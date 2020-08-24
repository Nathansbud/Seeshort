chrome.runtime.onMessage.addListener((req, sender, sendResponse) => {
    console.log(`Shortcut Selected: ${req}`)
    if(document.activeElement.tagName.toLowerCase() == 'textarea' || (document.activeElement.tagName.toLowerCase() == 'input' && document.activeElement.getAttribute('type') == 'text')) {
        document.activeElement.value += req.shortcut
    }

    return true
})

