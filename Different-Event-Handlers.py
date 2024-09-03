import sys
import re

# List of new event handlers and keywords
event_handlers = ['OnAfterprint', 'OnAfterscriptexecute', 'OnAnimationcancel', 'OnAnimationend', 'OnAnimationiteration', 'OnAnimationstart', 'OnAuxclick', 'OnBeforecopy', 'OnBeforecut', 'OnBeforeinput', 'OnBeforeprint', 'OnBeforescriptexecute', 'OnBeforetoggle', 'OnBeforeunload', 'OnBegin', 'OnBlur', 'OnCanplay', 'OnCanplaythrough', 'OnChange', 'OnClick', 'OnClose', 'OnContextmenu', 'OnCopy', 'OnCuechange', 'OnCut', 'OnDblclick', 'OnDrag', 'OnDragend', 'OnDragenter', 'OnDragexit', 'OnDragleave', 'OnDragover', 'OnDragstart', 'OnDrop', 'OnDurationchange', 'OnEnd', 'OnEnded', 'OnError', 'OnFocus', 'OnFocus', 'OnFocusin', 'OnFocusout', 'OnFormdata', 'OnFullscreenchange', 'OnHashchange', 'OnInput', 'OnInvalid', 'OnKeydown', 'OnKeypress', 'OnKeyup', 'OnLoad', 'OnLoadeddata', 'OnLoadedmetadata', 'OnLoadstart', 'OnMessage', 'OnMousedown', 'OnMouseenter', 'OnMouseleave', 'OnMousemove', 'OnMouseout', 'OnMouseover', 'OnMouseup', 'OnMousewheel', 'OnMozfullscreenchange', 'OnPagehide', 'OnPageshow', 'OnPaste', 'OnPause', 'OnPlay', 'OnPlaying', 'OnPointercancel', 'OnPointerdown', 'OnPointerenter', 'OnPointerleave', 'OnPointermove', 'OnPointerout', 'OnPointerover', 'OnPointerrawupdate', 'OnPointerup', 'OnPopstate', 'OnProgress', 'OnRatechange', 'OnRepeat', 'OnReset', 'OnResize', 'OnScroll', 'OnScrollend', 'OnSearch', 'OnSeeked', 'OnSeeking', 'OnSelect', 'OnSelectionchange', 'OnSelectstart', 'OnShow', 'OnSubmit', 'OnSuspend', 'OnTimeupdate', 'OnToggle', 'OnToggle', 'OnTouchend', 'OnTouchmove', 'OnTouchstart', 'OnTransitioncancel', 'OnTransitionend', 'OnTransitionrun', 'OnTransitionstart', 'OnUnhandledrejection', 'OnUnload', 'OnVolumechange', 'OnWebkitanimationend', 'OnWebkitanimationiteration', 'OnWebkitanimationstart', 'OnWebkitmouseforcechanged', 'OnWebkitmouseforcedown', 'OnWebkitmouseforceup', 'OnWebkitmouseforcewillbegin', 'OnWebkitplaybacktargetavailabilitychanged', 'OnWebkittransitionend', 'OnWebkitwillrevealbottom', 'OnWheel']
keywords = ['confirm', 'alert', 'prompt']

# Read payload from stdin
for line in sys.stdin:
    payload = line.strip()

    # Define a regex pattern to capture the event handler and action part
    pattern = r'(.*?)(\w+)=\s*(confirm|alert|prompt)(.*)'

    # Find the match
    match = re.match(pattern, payload)
    if match:
        base_part, current_event_handler, current_keyword, action_part = match.groups()

        # Generate output with different event handlers and keywords
        for event in event_handlers:
            for keyword in keywords:
                # Create the new payload with the new event handler and keyword
                new_payload = f"{base_part}{event}={keyword}{action_part}"
                print(new_payload)
    else:
        print("Payload does not match the expected format.")
