var request = require("request"),
	cheerio = require("cheerio"),
	  url = "http://www.wunderground.com/cgi-bin/findweather/getForecast?&query=" + 02888;

request(url, function (error, response, body) {
	if(!error) {
		var $ = cheerio.load(body);
		// console.log($);
		console.log(body)
			temperature = $("[data-variable = 'temperature'] .wx-value").html();
		console.log("It's " + temperature + " degress F.");
	} else {
		console.log("We've seen an error" + error);
	}
});