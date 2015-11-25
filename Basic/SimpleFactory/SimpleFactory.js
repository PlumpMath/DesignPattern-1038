// basic function, the concrete product
function A( name ){
    this.name = name;
}

// the factory
function ObjectFactory(){
    var obj = {},
    //The first param is the object to create
    Constructor = Array.prototype.shift.call( arguments );

    //judge the prototype
    obj.__proto__ =  typeof Constructor .prototype === 'number'  ? Object.prototype : Constructor .pjrototype;

    //give the left params to the constructor
    var ret = Constructor.apply( obj, arguments );

    return typeof ret === 'object' ? ret : obj;

 }

//create factory
var a = ObjectFactory( A, 'svenzeng' );

//svenzeng
alert ( a.name );
