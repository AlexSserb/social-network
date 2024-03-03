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
                <button onClick="deleteLike(${postId})" class="btn btn-danger mr-md-3 mb-2 mb-md-0">
                    Don't like
                </button>
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
                <button onClick="like(${postId})" class="btn btn-danger mr-md-3 mb-2 mb-md-0">
                    Like
                </button>
                <div>${data.likes}</div>
            `;
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}


$(function() {
    $( "i" ).click(function() {
        $( "i,span" ).toggleClass( "press", 1000 );
    });
});