document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('loginForm');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Empêche la soumission du formulaire par défaut

        // Récupère les valeurs des champs
        const pseudo = document.getElementById('pseudo').value;
        const motdepasse = document.getElementById('motdepasse').value;

        // Affiche les valeurs dans la console pour débogage
        console.log('Pseudo:', pseudo);
        console.log('Mot de Passe:', motdepasse);

        // Simule la connexion (remplacez ceci par votre logique d'authentification)
        if (pseudo === 'admin' && motdepasse === 'admin') {
            alert('Connexion réussie !');
            // Redirige vers le tableau de bord (remplacez par l'URL de votre tableau de bord)
            window.location.href = 'index.html';
        } else {
            alert('Pseudo ou mot de passe incorrect.');
        }
    });
});
