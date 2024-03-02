function like(postId) {
    fetch(`http://127.0.0.1:5000/posts/like/${postId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            let element = document.getElementById(postId);
            element.innerHTML = `
                <button onClick="deleteLike(${postId})">Don't like</button>
                <div>${data.likes}</div>
            `;
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}

function deleteLike(postId) {
    fetch(`http://127.0.0.1:5000/posts/delete_like/${postId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            let element = document.getElementById(postId);
            element.innerHTML = `
                <button onClick="like(${postId})">Like</button>
                <div>${data.likes}</div>
            `;
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}
