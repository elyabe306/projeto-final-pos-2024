const fetchPostsButton = document.getElementById('fetch-posts');
const dataContainer = document.getElementById('data');

async function fetchPosts() {
  try {
    const response = await fetch('http://localhost:8000/posts/');
    
    if (!response.ok) {
      throw new Error(`Erro: ${response.status}`);
    }

    const posts = await response.json();
    displayPosts(posts);
  } catch (error) {
    console.error('Erro ao buscar os posts:', error);
    dataContainer.innerHTML = 'Falha ao carregar os posts.';
  }
}


function displayPosts(posts) {
  dataContainer.innerHTML = ''; 
  posts.forEach((post) => {
    const postElement = document.createElement('div');
    postElement.className = 'post';
    postElement.innerHTML = `
      <h3>${post.title}</h3>
      <p>${post.body}</p>
    `;
    dataContainer.appendChild(postElement);
  });
}

fetchPostsButton.addEventListener('click', fetchPosts);