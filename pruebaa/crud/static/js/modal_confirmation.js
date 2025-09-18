/**
 * Inicializa el modal de confirmación para un formulario específico
 * @param {string} formId - El ID del formulario a validar
 */
function initConfirmationModal(formId) {
    // Elementos DOM
    const form = document.getElementById(formId);
    const btnPreview = document.getElementById('btnPreview');
    const btnConfirm = document.getElementById('btnConfirm');
    const modalBody = document.getElementById('modalBody');
    
    // Verificar que existan los elementos necesarios
    if (!form || !btnPreview || !btnConfirm || !modalBody) {
        console.error('No se encontraron todos los elementos necesarios para el modal');
        return;
    }
    
    // Evento para mostrar el modal con los datos del formulario
    btnPreview.addEventListener('click', function() {
        // Limpiar el contenido anterior
        modalBody.innerHTML = '';
        
        // Obtener todos los campos del formulario
        const formElements = form.elements;
        let html = '<div class="container"><div class="row"><div class="col-12">';
        html += '<h6>Revise los datos antes de confirmar:</h6>';
        html += '<ul class="list-group">';
        
        // Recorrer los elementos del formulario
        for (let i = 0; i < formElements.length; i++) {
            const element = formElements[i];
            
            // Solo procesar campos con nombre y que no sean botones
            if (element.name && element.type !== 'button' && element.type !== 'submit') {
                let label = element.name;
                let value = element.value;
                
                // Buscar etiqueta asociada si existe
                const labelElement = document.querySelector(`label[for="${element.id}"]`);
                if (labelElement) {
                    label = labelElement.textContent.trim();
                }
                
                // Para campos select, obtener el texto seleccionado
                if (element.tagName.toLowerCase() === 'select' && element.selectedIndex >= 0) {
                    value = element.options[element.selectedIndex].text;
                }
                
                // Para checkboxes, mostrar "Sí" o "No"
                if (element.type === 'checkbox') {
                    value = element.checked ? 'Sí' : 'No';
                }
                
                // Agregar a la lista si no es el token CSRF
                if (element.name !== 'csrfmiddlewaretoken') {
                    html += `<li class="list-group-item"><strong>${label}:</strong> ${value}</li>`;
                }
            }
        }
        
        html += '</ul></div></div></div>';
        modalBody.innerHTML = html;
        
        // Mostrar el modal
        const modal = new bootstrap.Modal(document.getElementById('confirmModal'));
        modal.show();
    });
    
    // Evento para enviar el formulario al confirmar
    btnConfirm.addEventListener('click', function() {
        form.submit();
    });
}