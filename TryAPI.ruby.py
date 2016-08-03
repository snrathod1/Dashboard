require 'httparty'

token = "1c4b40471046fdb5d0ff81570c7564fe244940c2"

user = HTTParty.get "https://api.github.com/user", 
        :headers => { 
                        "Authorization" => "token #{token}",
                        "User-Agent" => "codecademy"    
                    }

puts "Hi, my username is #{user["login"]}"