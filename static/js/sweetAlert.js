async function warningDeleteGrupo(nombre,pk){

    console.log("warningDeleteGrupo");

    await Swal.fire({
        title: '¿Eliminar grupo '+nombre+'?',
        icon: 'warning',
        iconColor: 'red',
        showCancelButton: true,
        showConfirmButton: true,
        confirmButtonText: `Eliminar`,
        confirmButtonColor: 'red',
        
    }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) 
        { 
            var request = $.ajax({
                type: "GET",
                url: "eliminar_identificador/",
                data: {
                    csrfmiddlewaretoken: '{% csrf_token %}',
                    "identificador_id": pk                    
                },
            });
            request.done(function(response) {
                Swal.fire('Eliminado!', '', 'success')
                window.location.href = "../dashboardDocente/"
            });
            
        }
    })
};