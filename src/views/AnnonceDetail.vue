<template>

    <div @click="unFocus()" ref="topContainer" class="container article-detail-container">

        <template v-if="this.loading">
            <div id="loading-detail-gif" class="column has-text-centered">
                <img :src="loadingSvg" />
            </div>
        </template>

        <template v-else>
            <h2 class="detail-title-article is-primary">
                {{this.articleDetails.nom}}
            </h2>

            <hr>

            <div class="categorie-bloc is-flex">
                <p class="dateParution" v-text="this.formatageDate(articleDetails.date)"></p>
                <p @click="goToThread(articleDetails.categorie.id)" class="has-text-weight-bold" style="color:#485fc7;cursor:pointer"> • {{articleDetails.categorie.nom}}</p>
            </div>

            <figure class="image">
                <img :src="articleDetails.main_picture" class="main-picture-article" alt="Placeholder image">
            </figure>

            <div class="columns">
                <div class="column is-1"></div>
                <div class="column is-10 detail-description">
                    <p>{{articleDetails.main_description}}</p>
                </div>
            </div>

            <div class="has-text-centered">
                <button class="button is-medium is-hidden-mobile buyCall">Je le veux !</button>
                <button class="button is-hidden-tablet buyCall">Je le veux !</button>
            </div>

            <hr>

            <!-- Facultatif descriptions + pictures + vidéo youtube -->

            <template v-if="articleDetails.video_link">
                <div class="columns">
                    <div class="column is-3"></div>
                    <div class="column is-6">
                        <iframe :src="'https://www.youtube.com/embed/'+articleDetails.video_link" width="100%" height="500px" frameborder="0" allowfullscreen></iframe> 
                    </div>
                </div>
                <hr>
            </template>

            <div class="has-text-centered">
                <template v-if="articleDetails.second_picture">
                    <figure class="image image-facultatif">
                        <img :src="articleDetails.second_picture" class="main-picture-article" alt="Placeholder image">
                    </figure>
                </template>
                <template v-if="articleDetails.second_description">
                    <div class="columns">
                        <div class="column is-1"></div>
                        <div class="column is-10 detail-description">
                            <p>{{articleDetails.second_description}}</p>
                        </div>
                    </div>
                </template>

                <template v-if="articleDetails.third_picture">
                    <figure class="image image-facultatif">
                        <img :src="articleDetails.third_picture" class="main-picture-article" alt="Placeholder image">
                    </figure>
                </template>
                <template v-if="articleDetails.third_description">
                    <div class="columns">
                        <div class="column is-1"></div>
                        <div class="column is-10 detail-description">
                            <p>{{articleDetails.third_description}}</p>
                        </div>
                    </div>
                </template>

                <template v-if="articleDetails.fourth_picture">
                    <figure class="image image-facultatif">
                        <img :src="articleDetails.fourth_picture" class="main-picture-article" alt="Placeholder image">
                    </figure>
                </template>
                <template v-if="articleDetails.fourth_description">
                    <div class="columns">
                        <div class="column is-1"></div>
                        <div class="column is-10 detail-description">
                            <p>{{articleDetails.fourth_description}}</p>
                        </div>
                    </div>
                </template>

                <template v-if="articleDetails.fifth_picture">
                    <figure class="image image-facultatif">
                        <img :src="articleDetails.fifth_picture" class="main-picture-article" alt="Placeholder image">
                    </figure>
                </template>
                <template v-if="articleDetails.fifth_description">
                    <div class="columns">
                        <div class="column is-1"></div>
                        <div class="column is-10 detail-description">
                            <p>{{articleDetails.fifth_description}}</p>
                        </div>
                    </div>
                </template>

                <template v-if="articleDetails.sixth_picture">
                    <figure class="image image-facultatif">
                        <img :src="articleDetails.sixth_picture" class="main-picture-article" alt="Placeholder image">
                    </figure>
                </template>
                <template v-if="articleDetails.sixth_description">
                    <div class="columns">
                        <div class="column is-1"></div>
                        <div class="column is-10 detail-description">
                            <p>{{articleDetails.sixth_description}}</p>
                        </div>
                    </div>
                </template>
            </div>

            <!-- ---------------------- -->

            <div class="columns">
                <div class="column is-1"></div>
                <div class="column is-12 detail-description">
                    <div class="columns">
                        <div class="column is-5 features-block">
                            <h2 class="title-details has-text-weight-bold">
                                <svg class="feature-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M14.44 18.56H9.57C9.47136 18.5588 9.37381 18.5808 9.28523 18.6243C9.19665 18.6677 9.1195 18.7313 9.06 18.81C8.99107 18.882 8.94053 18.9697 8.91268 19.0654C8.88483 19.1612 8.88048 19.2622 8.9 19.36C9.02522 20.0928 9.40559 20.7577 9.97383 21.2371C10.5421 21.7165 11.2616 21.9795 12.005 21.9795C12.7484 21.9795 13.4679 21.7165 14.0362 21.2371C14.6044 20.7577 14.9848 20.0928 15.11 19.36C15.1292 19.263 15.1257 19.1628 15.0996 19.0674C15.0736 18.9719 15.0258 18.8838 14.96 18.81C14.8974 18.7322 14.8183 18.6694 14.7283 18.6262C14.6383 18.5829 14.5398 18.5603 14.44 18.56Z" fill="#A6A6EF"/>
                                    <path d="M16.17 3.48001C15.3985 2.85529 14.4967 2.41152 13.531 2.18135C12.5654 1.95118 11.5604 1.94047 10.59 2.15001C9.46012 2.39204 8.41375 2.92692 7.55582 3.70098C6.69789 4.47505 6.05858 5.46108 5.702 6.5602C5.34542 7.65932 5.28411 8.83288 5.52421 9.96317C5.76432 11.0935 6.29741 12.1408 7.07001 13C7.56268 13.5524 7.8458 14.2602 7.87001 15V15.5C7.8692 15.9555 8.01306 16.3994 8.28085 16.7679C8.54864 17.1363 8.92652 17.4102 9.36001 17.55C9.42928 17.5643 9.50073 17.5643 9.57 17.55H14.44C14.5126 17.5643 14.5874 17.5643 14.66 17.55C15.09 17.4058 15.464 17.1305 15.7294 16.7628C15.9949 16.3951 16.1385 15.9535 16.14 15.5V15C16.1505 14.2239 16.4418 13.4778 16.96 12.9C17.5449 12.2342 17.9896 11.4573 18.2673 10.6157C18.5451 9.77415 18.6502 8.88519 18.5764 8.00203C18.5027 7.11888 18.2516 6.25967 17.8381 5.47581C17.4246 4.69195 16.8573 3.99954 16.17 3.44001V3.48001ZM15.12 9.28C14.9397 9.28 14.7667 9.20836 14.6392 9.08084C14.5116 8.95331 14.44 8.78035 14.44 8.60001C14.4374 7.95369 14.1795 7.33459 13.7224 6.87757C13.2654 6.42055 12.6463 6.16264 12 6.16001C11.8197 6.16001 11.6467 6.08836 11.5192 5.96084C11.3916 5.83331 11.32 5.66035 11.32 5.48001C11.32 5.29966 11.3916 5.1267 11.5192 4.99917C11.6467 4.87165 11.8197 4.80001 12 4.80001C13.007 4.80264 13.972 5.20385 14.6841 5.91592C15.3962 6.62798 15.7974 7.59299 15.8 8.60001C15.7974 8.77955 15.7249 8.95101 15.598 9.07798C15.471 9.20495 15.2995 9.27742 15.12 9.28Z" fill="#A6A6EF"/>
                                </svg>
                                Fonctionnalités
                            </h2>
                            <p class="features">{{articleDetails.features}}</p>
                        </div>
                        <div class="column is-5">
                            <div class="last-call">
                                <template v-if="articleDetails.price">
                                    <p class="price-details">
                                        <svg class="price-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M21.57 5.1C21.43 3.69 20.31 2.56 18.9 2.43L14.52 2.01C13.6 1.92 12.69 2.25 12.03 2.91L2.92001 12.02C2.34001 12.6 2.01 13.37 2 14.18C1.99 14.99 2.28999 15.76 2.86999 16.33L7.66 21.13C8.24 21.71 8.99999 21.99 9.76999 21.99C10.56 21.99 11.36 21.69 11.97 21.08L21.08 11.97C21.74 11.31 22.07 10.4 21.99 9.48L21.57 5.1ZM15.66 6.48C16.17 5.96 17 5.97 17.52 6.48C18.03 6.99 18.03 7.82999 17.52 8.33999C17.26 8.59999 16.92 8.72 16.59 8.72C16.25 8.72 15.91 8.59999 15.66 8.33999C15.14 7.82999 15.14 6.99 15.66 6.48Z" fill="#A6A6EF"/>
                                        </svg>
                                        {{articleDetails.price}} €
                                    </p>
                                </template>
                                <button class="button is-medium is-hidden-mobile buyCall">Acheter maintenant</button>
                                <button class="button is-hidden-tablet buyCall">Acheter maintenant</button>
                                <p class="amz-link">Amazon.com</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <hr>
            <br>

            <!-- ------- RELATED ARTICLES ------- -->

        
            <template v-if="this.relatedArticles.length > 0">
                <h3 class="title is-3 is-hidden-mobile">Articles similaires</h3>
                <h3 class="title is-4 is-hidden-tablet">Articles similaires</h3>
                <div class="columns">
                    <template v-for="(article, index) in this.relatedArticles">
                        <div :key="index" class="column is-3">
                            <a style="color:black" @click="goToDetails(article.id)">
                                <figure class="image">
                                    <img :src="article.main_picture" class="preview-related-article" alt="Placeholder image">
                                </figure>
                                <p class="has-text-weight-bold preview-article-name">{{article.nom}}</p>
                                <template v-if="article.price">
                                    <p class="preview-article-price">{{article.price}} €</p>
                                </template>
                            </a>
                        </div>
                    </template>
                </div>

                <hr>
            </template>

            <!-- ------ COMMENTARY SECTION ------ -->

            <template v-if="this.comments.length > 0">
                <template v-for="(comment, index) in this.comments">
                    <div :key="index" class="columns">
                        <div class="column is-1"></div>
                        <div class="column is-9">
                            <div class="card commentary-response">
                                <div class="columns is-justify-content-space-between">
                                    <div class="commentary-name is-flex">
                                        <p class="commentary-icon">
                                            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <path d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM11.8 6.77C13.58 6.77 15.02 8.21 15.02 9.99C15.02 11.76 13.58 13.21 11.8 13.21C10.03 13.21 8.59 11.76 8.59 9.99C8.59 8.21 10.03 6.77 11.8 6.77ZM17.93 18.08C17.48 18.53 16.97 18.92 16.43 19.25C15.14 20.05 13.62 20.5 12 20.5C10.38 20.5 8.86001 20.05 7.57001 19.25C7.03001 18.92 6.52001 18.53 6.07001 18.08V17.89C6.07001 15.84 7.74 14.17 9.78 14.17H14.22C16.26 14.17 17.93 15.84 17.93 17.89V18.08Z" fill="rgb(166, 166, 239)"/>
                                            </svg>
                                        </p>
                                        <p style="margin-top: 2%">
                                            {{comment.author}}
                                        </p>
                                    </div>
                                    <div class="is-hidden-mobile">
                                        <button @click="reply()" class="button">Répondre</button>
                                    </div>
                                </div>
                                <div class="response-bloc-resp">
                                    <p class="commentary-date" v-text="formatageDate(comment.date, true)"></p>
                                    <div class="is-hidden-tablet">
                                        <button @click="reply()" class="button is-small" style="margin-top: -11%;">Répondre</button>
                                    </div>
                                </div>
                                <hr>
                                <p>{{comment.commentary}}</p>
                            </div>
                        </div>
                    </div>
                </template>
            </template>

            <div ref="commentarySection" class="columns">
                <div class="column is-1"></div>
                <div id="commentary-section" class="column is-9">
                    <p class="title is-4 is-hidden-mobile">Laisse un commentaire</p>
                    <p class="title is-5 is-hidden-tablet">Laisse un commentaire</p>
                    <textarea v-model="this.commentContent" ref="textAreaCommentary" class="textarea is-primary" placeholder="Que pensez-vous de cette Trouvaille ?"></textarea>

                    <br>

                    <div class="columns">
                        <div class="column is-4">
                            <div class="field">
                                <p class="control has-icons-left">
                                    <input v-model="this.commentAuthor" class="input is-primary" placeholder="Nom">
                                    <span class="icon is-small is-left">
                                        <svg width="35" height="35" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M12 2C6.49 2 2 6.49 2 12C2 17.51 6.49 22 12 22C17.51 22 22 17.51 22 12C22 6.49 17.51 2 12 2ZM11.8 6.77C13.58 6.77 15.02 8.21 15.02 9.99C15.02 11.76 13.58 13.21 11.8 13.21C10.03 13.21 8.59 11.76 8.59 9.99C8.59 8.21 10.03 6.77 11.8 6.77ZM17.93 18.08C17.48 18.53 16.97 18.92 16.43 19.25C15.14 20.05 13.62 20.5 12 20.5C10.38 20.5 8.86001 20.05 7.57001 19.25C7.03001 18.92 6.52001 18.53 6.07001 18.08V17.89C6.07001 15.84 7.74 14.17 9.78 14.17H14.22C16.26 14.17 17.93 15.84 17.93 17.89V18.08Z" fill="rgb(166, 166, 239)"/>
                                        </svg>
                                    </span>
                                </p>
                            </div>
                        </div>
                        
                        <div class="column is-4">
                            <div class="field">
                                <p class="control has-icons-left">
                                    <input v-model="this.commentEmail" class="input is-primary" placeholder="E-mail">
                                    <span class="icon is-small is-left">
                                        <svg width="35" height="35" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M11.18 12.06C11.67 12.54 12.34 12.54 12.83 12.06L19.15 5.78L20.32 4.61C19.88 4.38 19.39 4.25 18.86 4.25H5.15001C4.62001 4.25 4.13 4.38 3.69 4.61L4.86 5.78L11.18 12.06Z" fill="rgb(166, 166, 239)"/>
                                            <path d="M8.93001 11.94L3.67001 6.7L2.57001 5.61C2.21001 6.12 2.01001 6.73 2.01001 7.4V16.6C2.01001 17.16 2.16001 17.69 2.41001 18.14C2.42001 18.13 2.42001 18.13 2.43001 18.12L3.57001 17.03L8.93001 11.94Z" fill="rgb(166, 166, 239)"/>
                                            <path d="M14.09 12.92L13.89 13.12C13.35 13.65 12.68 13.92 12 13.92C11.33 13.92 10.66 13.65 10.12 13.12L9.99001 12.99L4.59 18.15L3.47001 19.21C3.46001 19.22 3.45 19.23 3.44 19.23C3.93 19.56 4.51001 19.75 5.15001 19.75H18.86C19.49 19.75 20.08 19.56 20.57 19.23L19.45 18.14L14.09 12.92Z" fill="rgb(166, 166, 239)"/>
                                            <path d="M21.45 5.61L20.35 6.7L15.15 11.86L20.45 17.03L21.6 18.15C21.86 17.7 22.01 17.16 22.01 16.6V7.4C22.01 6.73 21.81 6.12 21.45 5.61Z" fill="rgb(166, 166, 239)"/>
                                        </svg>
                                    </span>
                                </p>
                            </div>
                        </div>

                        <div class="column is-4">
                            <div class="field">
                                <p class="control has-icons-left">
                                    <input v-model="this.commentWebsite" class="input is-primary" placeholder="Website">
                                    <span class="icon is-small is-left">
                                        <svg width="35" height="35" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M18.25 2H5.75C3.68 2 2 3.68 2 5.75V18.25C2 20.32 3.68 22 5.75 22H18.25C20.32 22 22 20.32 22 18.25V5.75C22 3.68 20.32 2 18.25 2ZM9.7 10.27C10.81 9.16 12.62 9.16 13.73 10.27C14.02 10.57 14.02 11.04 13.73 11.33C13.44 11.63 12.96 11.63 12.67 11.33C12.14 10.81 11.28 10.81 10.76 11.33L7.15 14.94C6.62 15.47 6.62 16.33 7.15 16.85C7.67 17.38 8.53 17.38 9.06 16.85L10.56 15.35C10.86 15.06 11.33 15.06 11.62 15.35C11.92 15.64 11.92 16.12 11.62 16.41L10.12 17.92C9.56 18.47 8.83 18.75 8.1 18.75C7.37 18.75 6.64 18.47 6.09 17.92C4.97 16.8 4.97 15 6.09 13.88L9.7 10.27ZM14.31 13.73C13.75 14.28 13.02 14.56 12.29 14.56C11.56 14.56 10.83 14.28 10.27 13.73C9.98 13.43 9.98 12.96 10.27 12.67C10.57 12.37 11.04 12.37 11.33 12.67C11.86 13.19 12.72 13.19 13.25 12.67L16.86 9.06C17.38 8.53 17.38 7.66999 16.86 7.14999C16.33 6.61999 15.47 6.61999 14.94 7.14999L13.44 8.64999C13.15 8.93999 12.67 8.93999 12.38 8.64999C12.09 8.35999 12.09 7.88 12.38 7.59L13.88 6.08C15 4.97 16.8 4.97 17.92 6.08C19.03 7.2 19.03 9 17.92 10.12L14.31 13.73Z" fill="rgb(166, 166, 239)"/>
                                        </svg>
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>

                    <button @click="sendCommentary()" class="button is-primary has-text-weight-bold">Envoyer</button>
                </div>
            </div>
        </template>

    </div>

</template>

<script>
import { mapState } from 'vuex';

export default {
    name: 'AnnonceDetail',
    created() {
        this.$store.dispatch('articleDetails', this.$route.params.pk)
        .then(() => {
            var element = this.$refs.topContainer;
            element.scrollIntoView({block: "start"});
        });
    },
    data() {
      return {
        commentContent: null,
        commentAuthor: null,
        commentEmail: null,
        commentWebsite: null,
        loadingSvg: require('../assets/svg/loading.gif')
      }
    },
    computed: mapState ([
        'articleDetails',
        'relatedArticles',
        'comments',
        'loading'
    ]),
    components: {
    },
    methods: {
        formatageDate(date, hour=false) {
            const months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
            'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
            const today = new Date();
            var currentYear = today.getFullYear();
            var currentDay = String(today.getDate()).padStart(2, '0');
            var currentMonth = String(today.getMonth() + 1).padStart(2, '0');

            var year = date.substring(0,4)
            var month = months[parseInt(date.substring(5,7))-1]
            var day = date.substring(8,10)

            if (currentYear == year && currentDay == day && currentMonth == date.substring(5,7)) {
                if (hour) {
                    var hour = date.substring(11,13)
                    var minute = date.substring(14,16)
                    return ("Aujourd'hui à " + hour + "h" + minute)
                } else {
                    return ("Aujourd'hui")
                }
            } else {
                if (currentYear == year) {
                    if (hour) {
                        var hour = date.substring(11,13)
                        var minute = date.substring(14,16)
                        return(day + ' ' + month + ' à ' + hour + "h" + minute)
                    } else {
                        return(day + ' ' + month)
                    }
                    
                } else {
                    return(day + ' ' + month + ' ' + year)
                }
            }
        },

      goToThread(id) {
            this.$store.dispatch('perCategories', {'id':id, infoPage:null})
            .then({
                this:this.$router.push({ name: 'Accueil'})
            });
        },

      goToDetails(pk) {
        this.$store.dispatch('articleDetails', pk)
        .then(() => {
            var element = this.$refs.topContainer;
            element.scrollIntoView({block: "start"});
        });
      },

      reply() {
        var element = this.$refs.commentarySection;
        var textArea = this.$refs.textAreaCommentary;
        element.scrollIntoView({block: "start"});
        textArea.focus();
      },

      sendCommentary() {
        this.$store.dispatch('sendCommentary', {
        'id': this.articleDetails.id, 
        'commentAuthor': this.commentAuthor, 
        'commentContent': this.commentContent,
        'commentEmail': this.commentEmail, 
        'commentWebsite': this.commentWebsite
        })
        .then(response => {
            this.commentAuthor = null;
            this.commentContent = null;
            this.commentEmail = null;
            this.commentWebsite = null;
        })
      },

      unFocus() {
        this.$store.dispatch('resetSearchCompletion');
        }
      
    }
}
</script>

<style lang="scss">

    #loading-detail-gif {
        margin-top:10%;
        margin-bottom:20%;
    }

    #loading-detail-gif img {
        width:120px;
    }

    .detail-title-article {
        margin-top:5%;
        font-size:2em;
        font-weight: bold;
    }

    .dateParution {
        font-style: italic;
        margin-right:0.5%;
    }

    .main-picture-article {
        max-height: 600px;
        object-fit: contain;
        background-position: center center;
        border-radius: 20px;
    }

    .detail-description {
        margin-top:3%;
        font-size: 1.2em;
    }

    .buyCall {
        background-color: #2b783e!important;
        border-color: #2b783e!important;
        color:white!important;
        font-weight: bold;
    }

    .features {
        white-space: pre-wrap;
    }

    .feature-icon {
        width: 50px;
        margin-bottom: -1%;
    }

    .features-block {
        border-right: 0.4px solid;
        margin-right: 5%;
        border-color: #e4e4e4;
    }

    .title-details {
        font-weight: bold;
        font-size: 2em;
        margin-bottom:4%;
    }

    .price-details {
        color: #e23a05;
        font-weight: bold;
        font-size: 1.5em;
        margin-top:5%;
        margin-bottom:2%;
    }

    .price-icon {
        width: 30px;
        margin-bottom:-1.2%;
    }

    .amz-link {
        color:grey;
        font-size: 0.7em;
        margin-top:2%;
    }

    .last-call {
        padding: 3%;
    }

    .image-facultatif {
        width: 60%;
        margin-left: auto;
        margin-right: auto;
    }

    .preview-article-name {
        margin-top:2%;        
    }

    .preview-related-article {
        border-radius:10px;
        height: 295px!important;
    }

    .preview-article-price {
        font-size:1.1em;
        color:#2b783e;
        margin-top:2%;
    }

    #commentary-section {
        background-color: #f6f6f6;
        border-radius:10px;
        margin-top:2%;
        padding:3%;
    }

    .commentary-response {
        padding:2%;
    }

    .commentary-icon svg {
        width: 35px;
        height: 35px;
    }

    .commentary-name {
        font-weight: bold;
        font-size: 1.1em;
        color:#A6A6EF;
    }

    .commentary-date {
        color:grey;
        font-size:0.8em;
        margin-top:-1%;
    }

    @media only screen and (max-width:768px) {
        .detail-title-article {
            font-size:1.6em;
        }

        .article-detail-container {
            padding:3%;
        }

        .categorie-bloc {
            margin-bottom: 2%;
        }

        .title-details {
            font-size:1.5em;
        }

        .features-block {
            border-right: none;
        }

        .last-call {
            text-align: center;
        }

        .image-facultatif {
            width: 100%;
        }

        .card {
            margin-left: 0%!important;
            margin-right: 0%!important;
        }

        .response-bloc-resp {
            display: flex;
            justify-content: space-between;
        }

        .commentary-name {
            margin-left: 2%;
            margin-top: 3%;
        }

        .commentary-response {
            padding-bottom: 3%;
        }

        .price-details {
            font-size:1.4em;
        }

        .feature-icon {
            margin-bottom: -3%;
        }
    }
</style>