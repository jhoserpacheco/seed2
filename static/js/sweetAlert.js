
async function warningDeleteGrupo(nombre,pk,padre){
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
                url: "/eliminar_grupo/",
                data: {
                    csrfmiddlewaretoken: '{% csrf_token %}',
                    "identificador_id": pk                    
                },
            });
            request.done(function(response) {
                Swal.fire({
                    title:'Eliminado!',
                    icon:'success',
                    showConfirmButton: true,
                    confirmButtonText: 'Ok',
                    //confirmButtonColor: 'green',
                    timer:1500,
                    timerProgressBar: true,

                }).then((result) => {
                    if (padre=="1") {                        
                        window.location.href = "../create";
                    }
                    else
                        location.reload();
                })                
            });
            
        }
    })
};

async function warningDeleteTema(nombre,pk,padre){
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
                url: "/eliminar_tema/",
                data: {
                    csrfmiddlewaretoken: '{% csrf_token %}',
                    "identificador_id": pk                    
                },
            });
            request.done(function(response) {
                Swal.fire({
                    title:'Eliminado!',
                    icon:'success',
                    showConfirmButton: true,
                    confirmButtonText: 'Ok',
                    //confirmButtonColor: 'green',
                    timer:1500,
                    timerProgressBar: true,

                }).then((result) => {
                    if (padre=="1") {                        
                        window.location.href = "../../create";
                    }
                    else
                        location.reload();
                })                
            });
            
        }
    })
};

async function warningDeleteActividad(nombre,pk,padre){
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
                url: "/eliminar_actividad/",
                data: {
                    csrfmiddlewaretoken: '{% csrf_token %}',
                    "identificador_id": pk                    
                },
            });
            request.done(function(response) {
                Swal.fire({
                    title:'Eliminado!',
                    icon:'success',
                    showConfirmButton: true,
                    confirmButtonText: 'Ok',
                    //confirmButtonColor: 'green',
                    timer:1500,
                    timerProgressBar: true,

                }).then((result) => {
                    if (padre=="1") {                        
                        window.location.href = "../../create";
                    }
                    else
                        location.reload();
                })                
            });
            
        }
    })
};