async function warningDeleteGrupo(nombre){

    console.log("warningDeleteGrupo");

    await Swal.fire({
        title: '¿Eliminar grupo '+nombre+'?',
        icon: 'warning',
        iconColor: 'red',
        showCancelButton: true,
        showConfirmButton: true,
        confirmButtonText: `Eliminar`,
        
        
    }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          Swal.fire('Eliminado!', '', 'success')
        }
      })
};