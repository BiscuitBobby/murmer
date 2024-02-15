from functions import *
from elements import *

window.setWindowTitle('Murmer')

window.setAcceptDrops(True)
window.setLayout(layout)

window.dragEnterEvent = dragEnterEvent
window.dropEvent = dropEvent
window.dragLeaveEvent = dragLeaveEvent

window.show()
app.exec()

