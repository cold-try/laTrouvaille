<template>
    <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a @click="resetNavigation()">
                <img src="../assets/website-logo.png">
            </a>

            <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div id="navbar-menu" class="navbar-menu">
            <div class="navbar-start">
                <a @click="resetNavigation()" class="navbar-item navbar-elem">
                    Accueil
                </a>

                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link navbar-elem">
                        Catégories
                    </a>

                    <div class="navbar-dropdown">
                        <template v-if="this.categories.length > 0">
                            <template v-for="(categorie, index) in this.categories">
                                <a :key=index @click="goToThread(categorie.id)" class="navbar-item navbar-line">
                                    {{categorie.nom}}
                                </a>
                            </template>
                        </template>
                        <template v-else>
                            <a class="navbar-item">Aucune catégorie pour le moment.</a>
                        </template>
                    </div>
                </div>

                <a class="navbar-item navbar-elem">
                    Notre sélection
                </a>

                <a class="navbar-item navbar-elem">
                    Vu sur les réseaux sociaux
                </a>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="control has-icons-right">
                        <input class="input is-medium" type="email" placeholder="Recherche ...">
                        <span class="icon is-medium is-right search-button">
                            <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M10.97 5.91C8.18003 5.91 5.91003 8.18 5.91003 10.97C5.91003 13.76 8.18003 16.04 10.97 16.04C13.77 16.04 16.04 13.76 16.04 10.97C16.04 8.18 13.77 5.91 10.97 5.91Z" fill="grey"/>
                                <path d="M21.78 20.72L17.82 16.76C19.14 15.19 19.94 13.18 19.94 10.97C19.94 6.03 15.92 2 10.97 2C6.03 2 2 6.03 2 10.97C2 15.92 6.03 19.94 10.97 19.94C13.18 19.94 15.2 19.14 16.76 17.82L20.72 21.78C20.87 21.93 21.06 22 21.25 22C21.44 22 21.63 21.93 21.78 21.78C22.07 21.49 22.07 21.01 21.78 20.72ZM10.97 17.54C7.35 17.54 4.41 14.59 4.41 10.97C4.41 7.35 7.35 4.41 10.97 4.41C14.59 4.41 17.54 7.35 17.54 10.97C17.54 14.59 14.59 17.54 10.97 17.54Z" fill="grey"/>
                            </svg>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import { mapState } from 'vuex';

export default {
    name: 'Navbar',
    data() {
      return {
      }
    },
    computed: mapState ([
        'categories'
    ]),
    components: {
    },
    methods: {
        goToThread(id) {
            this.$store.dispatch('perCategories', {'id':id, infoPage:null});
        },

        resetNavigation() {
            this.$store.dispatch('lastEntries')
            .then({
                this:this.$router.push({ name: 'Accueil'})
            });
        }
    }
}
</script>

<style lang="scss">
    @font-face {
        font-family: "leagueSpartan";
        src: url("../../public/fonts/LeagueSpartan-Bold.otf");
    }

    .navbar-elem {
        font-size:1.4em;
        font-family: 'leagueSpartan';
        color:black!important;
    }

    #navbar-menu {
        margin-left:3%;
    }

    .navbar-line {
        font-size:1.3em;
    }

    .search-button {
        cursor: pointer;
    }

</style>

