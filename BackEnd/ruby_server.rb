```ruby
require 'sinatra'
require 'json'
require_relative '../Motorhead/configuration'
require_relative '../Motorhead/user_profile'
require_relative '../Motorhead/conversation'
require_relative '../Alana/alana'

class MotorStackServer < Sinatra::Base
  set :port, 8080

  before do
    content_type :json
  end

  post '/api/chat' do
    data = JSON.parse(request.body.read)
    user_id = data['user_id']
    input = data['input']

    alana = Alana.new('Alana', 'AI')
    response = alana.chat(input, user_id)

    response.to_json
  end

  get '/api/user/:id' do
    user_id = params[:id]
    user = Motorhead::UserProfile.find(user_id)

    user.to_json
  end

  get '/api/conversation/:id' do
    user_id = params[:id]
    conversation = Motorhead::Conversation.for_user(user_id)

    conversation.to_json
  end

  run! if app_file == $0
end
```