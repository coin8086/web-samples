require './app'
require './middleware'

use Middleware
run App.new
