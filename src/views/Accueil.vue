<template>


  <div ref="articlesTop" class="container">

    <h2 class="title-top has-text-weight-bold">
      <template v-if="this.fromCategory">
        <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M3.78003 12.75H6.11002V20.22C6.11002 21.2 6.91005 22 7.89005 22H8.92004C9.90004 22 10.69 21.2 10.69 20.22V12.75H17.48C17.69 12.75 17.9 12.66 18.04 12.5L20.78 9.41C21.04 9.13 21.04 8.7 20.78 8.42L18.04 5.33C17.9 5.17 17.69 5.08 17.48 5.08H10.69V3.78C10.69 2.8 9.90004 2 8.92004 2H7.89005C6.91005 2 6.11002 2.8 6.11002 3.78V5.08H3.78003C3.36003 5.08 3.03003 5.42 3.03003 5.83V12C3.03003 12.41 3.36003 12.75 3.78003 12.75ZM7.61002 3.78C7.61002 3.63 7.74005 3.5 7.89005 3.5H8.92004C9.07004 3.5 9.19003 3.63 9.19003 3.78V5.08H7.61002V3.78ZM7.61002 12.75H9.19003V20.22C9.19003 20.37 9.07004 20.5 8.92004 20.5H7.89005C7.74005 20.5 7.61002 20.37 7.61002 20.22V12.75Z" fill="#A6A6EF"/>
        </svg>
        {{this.fromCategory}}
      </template>

      <template v-else>
        <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M19.19 5.03H16.11C15.7 5.03 15.36 5.37 15.36 5.78V8.11H11.29C11.54 7.54 11.72 6.95 11.72 6.4C11.72 4.57 10.23 3.08 8.39999 3.08C6.56999 3.08 5.08 4.57 5.08 6.4C5.08 6.94 5.26 7.54 5.52 8.11H4.81C3.26 8.11 2 9.37 2 10.92V18.11C2 19.66 3.26 20.92 4.81 20.92H19.19C20.74 20.92 22 19.66 22 18.11V7.84C22 6.29 20.74 5.03 19.19 5.03ZM8.39999 5.6C8.88999 5.6 9.28999 6 9.28999 6.49C9.28999 6.98 8.88999 7.37 8.39999 7.37C7.90999 7.37 7.52 6.98 7.52 6.49C7.52 6 7.90999 5.6 8.39999 5.6ZM10.22 19.42H4.81C4.09 19.42 3.5 18.83 3.5 18.11V14.75H6.86C7.04 14.75 7.14 14.85 7.14 14.89C7.14 15.78 7.94 16.52 8.92 16.52H9.94C10.13 16.52 10.22 16.62 10.22 16.65V19.42ZM19.19 19.42H11.72V16.65C11.72 15.75 10.92 15.02 9.94 15.02H8.92C8.74 15.02 8.64 14.92 8.64 14.89C8.64 13.99 7.84 13.25 6.86 13.25H3.5V10.92C3.5 10.2 4.09 9.61 4.81 9.61H6.35001C6.90001 10.45 7.46999 11.12 7.67999 11.35C7.85999 11.55 8.12999 11.67 8.39999 11.67C8.67999 11.67 8.95001 11.55 9.13 11.35C9.33 11.12 9.91001 10.45 10.46 9.61H15.36V16.06C15.36 16.47 15.7 16.81 16.11 16.81H19.19C19.91 16.81 20.5 17.4 20.5 18.11C20.5 18.83 19.91 19.42 19.19 19.42Z" fill="#A6A6EF"/>
        </svg>
        Nos dernières trouvailles
      </template>
    </h2>

    <hr>
    
    <div class="columns is-12 articles-container">
      <template v-if="this.articles.length > 0">
        <template v-for="(article, index) in this.articles" :key="index">

          <div class="column is-4">
            <div class="card">
              <div class="card-image preview-article-div">
                <figure class="image" @click="goToDetails(article.id)">
                  <img :src="article.main_picture" class="preview-article" alt="Placeholder image">
                </figure>
              </div>

              <div class="card-content content-article-div">
                <div style="cursor:pointer" @click="goToDetails(article.id)">
                  <p class="title is-4">{{article.nom}}</p>

                  <div class="content description-article">
                    {{article.main_description}}
                    <br>
                  </div>
                </div>

                <div>
                  <template v-if="article.price">
                    <div class="price-block">
                      <p class="price">{{article.price}} €</p>
                    </div>
                    <button @click="goToDetails(article.id)" class="button buy-block-button">J'ACHETE</button>
                  </template>

                  <template v-else>
                    <button @click="goToDetails(article.id)" class="button more-block">Lire plus +</button>
                  </template>
                </div>

              </div>
            </div>
          </div>

        </template>

        <template v-if="this.totalPages > 1">
          <div id="pagination" class="container column is-12">
            <nav class="pagination is-rounded is-centered" role="navigation" aria-label="pagination">
              <a v-if="pageLink.previous" class="pagination-previous is-hidden-mobile" 
              @click="loadNewPage(pageLink.previous)">
                Précedent
              </a>
              <a v-else class="pagination-previous is-hidden-mobile" disabled>Précedent</a>
              <ul class="pagination-list">
                <li>
                  <a class="pagination-link" aria-label="Goto page 1" 
                  v-if="currentPage==1"
                  disabled>
                    1
                  </a>
                  <a class="pagination-link" aria-label="Goto page 1" v-else
                  @click="loadNewPage(1)">
                    1
                  </a>
                </li>
                <li><span class="pagination-ellipsis">&hellip;</span></li>
                <li v-if="currentPage==1"><a class="pagination-link" disabled>1</a></li>
                <li v-else>
                  <a class="pagination-link" v-text="currentPage - 1" 
                  @click="loadNewPage(currentPage - 1)">
                  </a>
                </li>
                <li><a class="pagination-link is-current" aria-current="page">{{currentPage}}</a></li>
                <li v-if="pageLink.next">
                  <a class="pagination-link" v-text="currentPage + 1" 
                  @click="loadNewPage(currentPage + 1)">
                  </a>
                </li>
                <li v-else><a class="pagination-link" v-text="currentPage + 1" disabled></a></li>
                <li><span class="pagination-ellipsis">&hellip;</span></li>
                <li>
                  <a class="pagination-link" 
                  v-if="this.totalPages==currentPage"
                  disabled>
                    {{totalPages}}
                  </a>
                  <a class="pagination-link" 
                  v-else
                  @click="loadNewPage(this.totalPages)">
                    {{totalPages}}
                  </a>
                </li>
              </ul>
              <a v-if="pageLink.next" class="pagination-next is-hidden-mobile" 
              @click="loadNewPage(pageLink.next)">
                Suivant
              </a>
              <a v-else class="pagination-next is-hidden-mobile" disabled>Suivant</a>
            </nav>
          </div>
        </template>

      </template>
    </div>

  </div>



</template>

<script>
// @ is an alias to /src
import { mapState } from 'vuex';

export default {
  name: 'Accueil',
  created() {
    this.$store.dispatch('lastEntries');
  },
  computed: mapState([
    'articles',
    'totalPages',
    'pageLink',
    'currentPage',
    'fromCategory',
    'categoryId'
  ]),
  components: {
  },
  methods: {
    goToDetails(pk) {
      this.$router.push({ name: 'AnnonceDetail', params: {pk: pk} });
    },

    loadNewPage(dataPage) {
      if (this.fromCategory) {
        if(typeof(dataPage) == 'number') {
          this.$store.dispatch('perCategories', {'id':this.categoryId, infoPage:dataPage});
        } else {
          this.$store.dispatch('lastEntries', dataPage);
        }
      } else {
        this.$store.dispatch('lastEntries', dataPage);
      }
      this.goTop();
    }, 

    goTop() {
      var element = this.$refs.articlesTop;
      element.scrollIntoView({block: "start"}); 
    },
  }
}
</script>

<style lang="scss">

  @font-face {
    font-family: "leagueSpartan";
    src: url("../../public/fonts/LeagueSpartan-Bold.otf");
  }

  .title-top {
    font-size:1.7em;
    margin-top:2%;
    margin-bottom:2%;
  }

  .title-icon {
    margin-bottom:-0.9%;
    width: 55px;
  }

  .articles-container {
    flex-wrap: wrap;
  }

  .preview-article-div {
    height:430px;
  }

  .preview-article {
    object-fit: cover;
    cursor: pointer;
  }

  .content-article-div {
    height: 275px;
  }

  .description-article {
    position:relative;
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: pre-wrap;
    height: 130px;
  }

  .description-article::before {
    content: " ";
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0px;
    height: 55px;
    background: linear-gradient(to bottom,  rgba(255,255,255,.5) 0%,rgba(255,255,255,1) 100%); 
  }

  .buy-block-button {
    position: absolute!important;
    bottom: 0px;
    right: 0;
    background-color:#2b783e!important;
    border-color: #2b783e!important;
    color:white!important;
    font-weight: bold;
  }

  .price-block {
    position: absolute!important;
    bottom: 0px;
    left: 0;
    background-color:#fcb900;
    padding:1%;
    padding-left:3%;
    padding-right:3%;
    font-size:1.1em;
    border-radius: 0.25rem;
  }

  .more-block {
    position: absolute!important;
    bottom: 0px;
    right: 0;
    padding:1%;
    padding-left:3%;
    padding-right:3%;
    font-size:1.1em;
    border-radius: 0.25rem;
  }

  .more {
    color:white;
    font-weight: bold!important;
  }

  #pagination {
    margin-top:5%;
  }

  .is-current {
    background-color:#A6A6EF!important;
    border-color: #A6A6EF!important;
  }
  
</style>
