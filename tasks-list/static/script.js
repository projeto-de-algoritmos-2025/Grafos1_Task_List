// function createTask() {
//     const id = document.getElementById('id').value;
//     const name = document.getElementById('name').value;
//     const description = document.getElementById('description').value;
  
//     const tarefa = {
//       id: parseInt(id),
//       name: name,
//       description: description
//     };
  
//     fetch('/cadastrar-tarefa', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(tarefa)
//     })
//     .then(res => res.json())
//     .then(data => {
//       document.getElementById('mensagem').innerText = data.mensagem;
//     });
//   }