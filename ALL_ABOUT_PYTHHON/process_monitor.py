import ctypes
from ctypes import CFUNCTYPE, c_int, c_ulong, byref, wintypes

# Define constants
WH_SHELL = 10
HSHELL_WINDOWCREATED = 1

# Callback function signature
ShellProc = CFUNCTYPE(c_int, c_ulong, wintypes.LPARAM, wintypes.LPARAM)

def hook_proc(nCode, wParam, lParam):
    if nCode == HSHELL_WINDOWCREATED:
        hwnd = wParam
        process_id = ctypes.wintypes.DWORD()
        thread_id = ctypes.windll.user32.GetWindowThreadProcessId(hwnd, byref(process_id))
        print(f"New process created with ID: {process_id.value}")

    return ctypes.windll.user32.CallNextHookEx(hook_id, nCode, wParam, lParam)

def main():
    # Set up the hook
    hook_id = ctypes.windll.user32.SetWindowsHookExA(
        WH_SHELL,
        ShellProc(hook_proc),
        None,  # The hook procedure is associated with all existing threads running in the same desktop as the calling thread.
        0
    )

    if not hook_id:
        print("Failed to set the hook")
        exit()

    try:
        # Enter the message loop to keep the script running
        msg = ctypes.wintypes.MSG()
        while ctypes.windll.user32.GetMessageW(byref(msg), 0, 0, 0) != 0:
            ctypes.windll.user32.TranslateMessage(byref(msg))
            ctypes.windll.user32.DispatchMessageW(byref(msg))

    finally:
        # Clean up the hook
        ctypes.windll.user32.UnhookWindowsHookEx(hook_id)

if __name__ == "__main__":
    main()
