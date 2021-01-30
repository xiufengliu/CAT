/*!
 * BOMB RISK ELICITATION TASK (BRET) APP
 * 
 * @author Armin Pfurtscheller
 * @license MIT
 */

(function(angular){

	//
	// ANGULAR
	//

	// check if angular core is availble
	if( typeof angular === 'undefined' )
	{
		throw Error('Cannot initialize bomb task without angular!');
		return;
	}

	//
	// MODULE
	//

	// initialize angular module for app
	var app = angular.module('bombTask',[]);

	//
	// CONSTANTS
	//
	app.constant('DEFAULT_NUM_ROWS',10);
	app.constant('DEFAULT_NUM_COLS',10);
	app.constant('DEFAULT_WIDTH','50px');
	app.constant('DEFAULT_HEIGHT','50px');

	//
	// CONTROLLER
	//

	/**
	 * @constructor
	 */
	var BombTaskController = function($scope,$filter,$interval,$injector)
		{
			this._storageKey = 'bret_state';

			this.$injector = $injector;
			this.$interval = $interval;
			this.$filter = $filter;
			this.$scope = $scope;
			this.init();
		};

	/**
	 * @property {Array.<String>} $inject
	 */
	BombTaskController.$inject = ['$scope','$filter','$interval','$injector'];

	/**
	 * Initializes matrix array and random bomb.
	 * @return {Void}
	 */
	BombTaskController.prototype.init = function()
		{
			// init internal members
			this._initSettings();
			this._initMatrix();
			this._initBomb();
		};


	/**
	 * Updates internal cards collection stack.
	 * @return {Void}
	 */
	BombTaskController.prototype.update = function(incolumn)
		{
		    this.resolved = true;
			for (var i=0; i<this.matrix.length; ++i){
			    var columns = this.matrix[i];
                for (var j=0; j<columns.length; ++j){
                    var column = columns[j];
			        //column.$$resolved = true;
			        column.$$disabled = true;
			        /*if (angular.equals(column, incolumn)){
			            column.$$active = true;
			        }*/
                }
            }

            this.hit_bomb = this.isBomb(incolumn)?1:0;
            incolumn.$$active = true;

		};


	/**
	 * Checks if this column equals current bomb.
	 * @param {Object} column The column to check.
	 * @return {Boolean}
	 */
	BombTaskController.prototype.isBomb = function(column)
		{
		    for (var i=0; i<this.bombs.length; ++i){
                if(angular.equals(this.bombs[i],column))
                    return true;
			}
			return false;
		};


	/**
	 * @ignore
	 */
	BombTaskController.prototype._getColumn = function(data)
		{
			// for data-binding!
			var row = data.row-1,
				col = data.col-1;

			return this.matrix[row][col];
		};

	/**
	 * @ignore
	 */
	BombTaskController.prototype._getConstant = function(name)
		{
			if( this.$injector.has(name) )
				return this.$injector.get(name);

			return this.$injector.get('DEFAULT_' + name);
		};


	/**
	 * @ignore
	 */
	BombTaskController.prototype._getState = function()
		{
			if( typeof sessionStorage !== "undefined" )
				return angular.fromJson(sessionStorage.getItem(this._storageKey));

			return null;
		};

	/**
	 * @ignore
	 */
	BombTaskController.prototype._setState = function(data)
		{
			if( typeof sessionStorage !== "undefined" )
				sessionStorage.setItem(this._storageKey,angular.toJson(data));
		};

	/**
	 * @ignore
	 */
	BombTaskController.prototype._removeState = function()
		{
			if( typeof sessionStorage !== "undefined" )
				sessionStorage.removeItem(this._storageKey);
		};

	/**
	 * @ignore
	 */
	BombTaskController.prototype._persist = function()
		{

			//this._setState(state);
		};


	/**
	 * @ignore
	 */
	BombTaskController.prototype._initSettings = function()
		{
			this.width = this._getConstant('WIDTH');
			this.height = this._getConstant('HEIGHT');
			this.rows = this._getConstant('NUM_ROWS');
			this.cols = this._getConstant('NUM_COLS');
			this.num_bombs = this._getConstant('NUM_BOMBS');
			this.resolved = false;
			this.hit_bomb = 0;
		};


	/**
	 * @ignore
	 */
	BombTaskController.prototype._initMatrix = function()
		{
			this.matrix = [];
			for( var i=0; i<this.rows; i++ )
			{
				var columns = [];
				for( var j=0; j<this.cols; j++ )
				{
					var data = { 
						row: i+1, 
						col: j+1 
					};

					columns.push(data);
				}

				this.matrix.push(columns);
			}
		};

	/**
	 * @ignore
	 */
	BombTaskController.prototype._initBomb = function()
		{
		    var tempArray = [];
		    for (var i=0; i<this.rows; ++i){
		        for (var j=0; j<this.cols; ++j){
		            tempArray.push([i, j]);
		        }
		    }
         var inds = this._shuffleArray(tempArray);

         this.bombs = [];
		 for (var i=0; i<this.num_bombs; ++i){
                this.bombs.push(this.matrix[inds[i][0]][inds[i][1]]);
			}
		};


	/**
	 * @ignore
	 */
	BombTaskController.prototype._getRandom = function(min,max)
		{
			return Math.floor(Math.random() * (max-min+1) + min);
		};

	/**
	 * @ignore
	 */
	BombTaskController.prototype._pushRandom = function(array,value)
		{
			// Inside-Out Shuffle Algorithm
			var rand = this._getRandom(0,array.length);
			array.push(array[rand]);
			array[rand] = value;

			return array.length;
		};

	/**
	 * @ignore
	 */
	BombTaskController.prototype._shuffleArray = function(array)
		{
			// Fisher-Yates Shuffle Algorithm
			for( var i=array.length-1; i>0; i-- )
			{
				var rand = this._getRandom(0,i),
		       		temp = array[i];

		        array[i] = array[rand];
		        array[rand] = temp;
		    }

    		return array;
		};

	// register the controller for app
	app.controller('BombTaskController',BombTaskController);

	//
	// COMPONENT
	//



	/**
	 * @constructor
	 */
	var CardController = function(){};

	/**
	 * @var {Objet} model Card's model to write.
	 */
	CardController.prototype.model = null;


	/**
	 * @var {Boolean} isClickable Cards clickability.
	 */
	CardController.prototype.isClickable = true;

    CardController.prototype.isDisabled = false;
		/**
	 * @var {Boolean} isActive Current activity state.
	 */
	CardController.prototype.active = false;
	
	/**
	 * Toggles card's current activity state.
	 * @return {Void}
	 */
	CardController.prototype.toggle = function()
		{

			if(!this.isClickable || this.isDisabled)
				return;

			this.active = true;
			this.onToggle(this.model);
			this.isClickable = false
		};

	// register the controller for app
	app.directive('card',function(){
		return {
			scope: {
				model:'=card',
				onToggle:'&cardOnToggle',
				isActive:'=?cardIsActive',
				isDisabled:'=?cardIsDisabled',
				isClickable:'=?cardIsClickable'
			},
			restrict: 'A',
			transclude: true,
			bindToController: true,
			templateUrl: '/card.html',
			controller: CardController,
			controllerAs: 'cardController'
		};

	});
	

})(angular);