@ECHO ON
pyuic5 -x -o .\Dialog_updateFunc.py .\Dialog-updateFunc.ui
pyuic5 -x -o .\Dialog_updateEmbarque.py .\Dialog-updateEmbarque.ui
pyuic5 -x -o .\Dialog_deleteFunc.py .\Dialog-deleteFunc.ui
pyuic5 -x -o .\Dialog_deleteEmbarque.py .\Dialog-deleteEmbarque.ui
pyuic5 -x -o .\Dialog_cadastroEmbarque.py .\Dialog-cadastroEmbarque.ui
pyuic5 -x -o .\Dialog_cadastroFunc.py .\Dialog-cadastroFunc.ui
pyrcc5 -o .\principal_resource.py .\principal_resource.qrc
PAUSE