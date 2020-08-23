const iconTable = document.querySelector('table')
const iconDir = "icons"

window.onload = () => createIcons()

function emitShortcut(e) {    
    e.cancelBubble = true
    e?.stopPropagation()

    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, {shortcut: e.target.dataset.shortcut}, (res) => {})
    })    
}   

function createIcons() {
    chrome.runtime.getPackageDirectoryEntry((root) => {
        root.getDirectory(iconDir, {create: false}, (dir) => {
            const reader = dir.createReader()
            reader.readEntries((results) => buildTable(results.map(r => r.name)))
        })
    })
}


function buildTable(imgNames) {
    for(let img of imgNames.sort()) {
        const shortcutValue = `:${img.split('.png')[0]}:`

        const iconRow = document.createElement('tr')
        
        const shortcutCell = document.createElement('td')
        const shortcut = document.createElement('span')
        
        shortcut.textContent = shortcutValue

        shortcut.dataset.shortcut = shortcutValue
        shortcut.onclick = (e) => emitShortcut(e)

        shortcutCell.dataset.shortcut = shortcutValue
        shortcutCell.onclick = (e) => emitShortcut(e)
        shortcutCell.append(shortcut)

        const iconCell = document.createElement('td')
        const icon = document.createElement('img')
        icon.src = chrome.extension.getURL(`/${iconDir}/${img}`)    
        icon.width = '61'

        icon.dataset.shortcut = shortcutValue
        icon.onclick = (e) => emitShortcut(e)

        iconCell.dataset.shortcut = shortcutValue
        iconCell.onclick = (e) => emitShortcut(e)
        iconCell.append(icon)
        
        iconRow.append(shortcutCell, iconCell)
        iconTable.append(iconRow)
    }
}