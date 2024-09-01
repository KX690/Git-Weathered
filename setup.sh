#!/bin/bash



if ! command -v pre-commit &> /dev/null  
then
    echo "Pre-commit no está instalado. Procediendo con la instalación..." 
    pip install pre-commit  Instala 'pre-commit'
    
    if [ $? -eq 0 ]; then 
        echo "Pre-commit se instaló correctamente." 
        
        
        pre-commit install  Instala los hooks de pre-commit en el repositorio
    else
        echo "Hubo un error al instalar pre-commit." 
    fi
else
    echo "Pre-commit ya está instalado." 
    
   
    pre-commit install 
fi


if ! command -v black &> /dev/null   
then
    echo "Black no está instalado. Procediendo con la instalación..."  
    
    
    pip install black  
    
    if [ $? -eq 0 ]; then   
        echo "Black se instaló correctamente."  
    else
        echo "Hubo un error al instalar black."  
    fi
else
    echo "Black ya está instalado."  
fi
