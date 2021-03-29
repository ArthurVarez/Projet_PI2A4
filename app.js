const app = Vue.createApp({
	data () {
                return {
                	titre: "Projet Pi2A4",
                	sousTitre1: "Ressources",
                	choixID1: "ID (only if you want to display one particular ressource) :",
                	headers1: [ "ID", "GPU", "Memory"],
                	sousTitre2: "Add a Ressource",
                	warning1: "WARNING : ID value must be unique",
                	sousTitre3: "Reservations",
                	choixID2: "ID (only if you want to display one particular reservation) : ",
                	headers2: ["ID", "Begins", "Ends", "User Name" ],
                	sousTitre4: "Add a Reservation",
                	lesJours: [ 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
                	lesMois: [01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12],
                	lesAnnees: [2020, 2021, 2022, 2023, 2024],
                	lesHeures: [ 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                	sousTitre5: "Reserved Ressources",
                	headers3: ["Reservation's ID", "Ressource's ID", "GPU", "Memory"],
                	sousTitre6: "Reserve a Ressource",
                	warning2: "WARNING : Reservation ID value must be unique",
                
                    id2: "",
                    lesRessources: [["", "", ""],["", "", ""],["", "", ""]],
                    id: "",
                    quantiteMemoire: "",
                    quantiteGPU: "",
                    
                    id3: "",
                    lesReservations: [["", "", "","" ],["", "", "", ""],["", "", "", ""]],
                    jour2: "",
                    mois: "",
                    annee: "",
                    heure: "",
                    fjour2: "",
                    fmois: "",
                    fannee: "",
                    fheure: "",
                    date_debut: "",
                    date_fin: "",
                    nomUtilisateur: "",
                    
                    lesRessourcesReserve: [["", "", "","" ],["", "", "", ""],["", "", "", ""]],
                    idReservation: "",
                    idRessource: "",
                    nbGPU: "",
                    nbMemoire: "",                    
                }
            },
        
	
	methods:{
                ajouterMembre: function(){
                    this.liste.push(this.valeur)
                },
                supprimerMembre: function(){
                    index = this.liste.findIndex(element => element === String(this.valeur))
                    for (var i = 0; i < this.liste.length; i++){
                        if (this.valeur === this.liste[i]){
                            index = i
                        }
                    }
                    this.$delete(this.liste, index)
                    
                    
                },


                getRessources: function(){
                	if (this.id2 === ""){
	                	axios
    	            .get('http://localhost:5000/Ressource/', {headers:{"Access-Control-Allow-Origin": "*",'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',}})
        	        .then(response => this.lesRessources = response.data.Ressources)
            	    .catch(erreur => console.log(erreur))
                	}else{
                		axios
                	.get('http://localhost:5000/Ressource/' + String(this.id2) + '/', {headers:{"Access-Control-Allow-Origin": "*",'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',}})
                	.then(response => this.lesRessources = [response.data])
                	.catch(erreur => console.log(erreur))
                	}
                    
                },
                
                suppRessources: function(){
                	this.lesRessources=[["", "", ""],["", "", ""],["", "", ""]]
                },
                
                addRessource: function(){
                    axios
                .post('http://localhost:5000/Ressource/', { "id": this.id, "quantiteMemoire": this.quantiteMemoire, "quantiteGPU": this.quantiteGPU } , {headers:{"Access-Control-Allow-Origin": "*",'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',}})
                .then(response => console.log(response))
                .catch(erreur => console.log(erreur))
                },
                
                getReservations: function(){
                	if (this.id3 === ""){
	                	axios
    	            .get('http://localhost:5000/Reservation/', {headers:{"Access-Control-Allow-Origin": "*",'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',}})
        	        .then(response => this.lesReservations = response.data.Reservations)
            	    .catch(erreur => console.log(erreur))
                	}else{
                		axios
                	.get('http://localhost:5000/Reservation/' + String(this.id3) + '/', {headers:{"Access-Control-Allow-Origin": "*",'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',}})
                	.then(response => this.lesReservations = [response.data])
                	.catch(erreur => console.log(erreur))
                	}
                    
                },
                
                suppReservations: function(){
                	this.lesReservations=[["", "", "","" ],["", "", "", ""],["", "", "", ""]]
                },
                
                addReservation: function(){
                	//this.date_debut = String(this.jour1) + ", " + String(this.jour2) + " " + String(this.mois) + " " + String(this.annee) + " " + String(this.heure) + ":00:00 GMT"
                	//this.date_fin = String(this.fjour1) + ", " + String(this.fjour2) + " " + String(this.fmois) + " " + String(this.fannee) + " " + String(this.fheure) + ":00:00 GMT"
					this.date_debut = String(this.annee)+"-"+String(this.mois)+"-"+String(this.jour2) + " " + String(this.heure) + ":00:00" 
					this.date_fin = String(this.fannee)+"-"+String(this.fmois)+"-"+String(this.fjour2) + " " + String(this.fheure) + ":00:00" 
                    axios
                .post('http://localhost:5000/Reservation/', {"date_debut": this.date_debut, "date_fin": this.date_fin} , {headers:{"Access-Control-Allow-Origin": "*",'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',}})
                .then(response => console.log(response))
                .catch(erreur => console.log(erreur))
                },
                
                getRessourcesReserve: function(){
                	
	                	axios
    	            .get('http://localhost:5000/RessourceReserve/', {headers:{"Access-Control-Allow-Origin": "*",'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',}})
        	        .then(response => this.lesRessourcesReserve = response.data.RessourceReserve)
            	    .catch(erreur => console.log(erreur))
                },
                
                suppRessourcesReserve: function(){
                	this.lesRessourcesReserve=[["", "", "","" ],["", "", "", ""],["", "", "", ""]]
                },
                
                addRessourceReserve: function(){
                    axios
                .post('http://localhost:5000/RessourceReserve/', { "idReservation": this.idReservation, "idRessource": this.idRessource, "nbGPU": parseInt(this.nbGPU), "nbMemoire": parseInt(this.nbMemoire) } , {headers:{"Access-Control-Allow-Origin": "*",'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',}})
                .then(response => console.log(response))
                .catch(erreur => console.log(erreur))
                },
            },
})

app.mount('#app ')