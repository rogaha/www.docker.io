###
  This is the main script file. It can attach to the terminal
###


###
  Register the things
###

@webterm = $('#terminal').terminal(interpreter, basesettings)

###
  Start with the questions
###

# the index arr
questions = []


EVENT_TYPES =
  none: "none"
  start: "start"
  command: "command"
  next: "next"
  feedback: "feedback"
  complete: "complete"


stateObj = { foo: "bar" };

current_question = 0
next = () ->
  current_question++
  questions[current_question]()
  results.clear()
  @webterm.focus()

  if not $('#commandShownText').hasClass('hidden')
    $('#commandShownText').addClass("hidden")
    $('#commandHiddenText').removeClass("hidden").show()

  history.pushState(stateObj, "", "#" + current_question);
  data = { 'type': EVENT_TYPES.next }
  logEvent(data)

#  $('form *').focus(function(){ terminal.focus(false); });

  return


previous = () ->
  current_question--
  questions[current_question]()
  results.clear()
  @webterm.focus()
  return

results = {
  set: (htmlText, intermediate) ->
    if intermediate
      console.debug "intermediate text received"
      $('#results').addClass('intermediate')
      $('#buttonNext').hide()
    else
      $('#buttonNext').show()

    window.setTimeout ( () ->
      $('#resulttext').html(htmlText)
      $('#results').fadeIn()
      $('#buttonNext').removeAttr('disabled')
    ), 300

  clear: ->
    $('#resulttext').html("")
    $('#results').fadeOut('slow')
#    $('#buttonNext').addAttr('disabled')
}

logEvent = (data, feedback) ->
    ajax_load = "loading......";
    loadUrl = "/tutorial/api/";
    if not feedback
      callback = (responseText) -> $("#ajax").html(responseText)
    else
      callback = (responseText) ->
        results.set("Thank you for your feedback! We appreciate it!", true)
        $("#ajax").html(responseText)

    if not data then data = {type: EVENT_TYPES.none}
    data.question = current_question


    $("#ajax").html(ajax_load);
    $.post(loadUrl, data, callback, "html")



###
  Array of question objects
###

q = []


q.push ({
html: """
      <h2>Getting started</h2>
      <p>There are actually two programs, a Docker daemon, it manages al the containers, and the Docker client.
      The client acts as a remote control on the daemon. On most systems, like in this emulation, both run on the
      same host.</p>
      """
assignment: """
      <h2>Assignment</h2>
      <p>Check which Docker version is running</p>
      <p>This will help you verify the daemon is running. If you see which version is running you know you are all set.</p>
      """
tip: "try typing `docker` to see the full list of accepted arguments"
command_expected: ['docker', 'version']
result: """<p>Well done! Let's move to the next assignment.</p>"""
})

q.push ({
html: """
      <h2>Searching for images</h2>
      <p>The easiest way of getting started is to use a container image from someone else. Container images are
      available on the docker index and can be found using <em>docker search</em></p>
      """
assignment: """
      <h2>Assignment</h2>
      <p>Please search for an image called tutorial</p>
      """
command_expected: ['docker', 'search', 'tutorial']
result: """<p>You found it!</p>"""
tip: "the format is `docker search &lt;string&gt;`"
})

q.push ({
html: """
      <h2>Downloading container images</h2>
      <p>Container images can be downloaded just as easily, using <em>docker pull.</em></p>
      <p>The name you specify is made up of two parts: the <em>username</em> and the <em>repository name</em>,
      divided by a slash `/`.</p>
      <p>A group of special, trusted images can be retrieved by just their repository name.</p>
      """
assignment:
      """
      <h2>Assignment</h2>
      <p>Please download the tutorial image you have just found</p>
      """
command_expected: ['docker', 'pull', 'learn/tutorial']
result: """<p>Cool. Look at the results. You'll see that docker has downloaded a number of layers. In Docker all images (except the base image) are made up of several cumulative layers.</p>"""
tip: """Don't forget to pull the full name of the repository e.g. 'learn/tutorial'"""
})


q.push ({
html: """
      <h2>Hello world from a container</h2>
      <p>You should think about containers as an operating system in a box, except they do not need to be booted
      before you can run commands in them. Instead, they are started <em>by</em> running a process in them. They
      also stop as soon as the process completes<p>
      """
assignment: """
      <h2>Assignment</h2>
      <p>Make our freshly loaded container image output "hello world"</p>
      """
command_expected: ["docker", "run", "learn/tutorial", "echo"]
command_show: ["docker", "run", "learn/tutorial", 'echo "hello world"']

result: """<p>Great! Hellooooo World!</p>"""
intermediateresults: [
  """<p>You seem to be almost there. Did you give the command `echo "hello world"` """,
  """<p>You've got the arguments right. Did you get the command? Try <em>/bin/bash </em>?</p>"""
  ]
tip: """
     <p>The command `docker run` takes two arguments. An image name, and the command you want to execute within that
    image.</p>
    """
})

q.push ({
html: """
      <h2>Installing things in the container</h2>
      <p>Next we are going to install a simple program in the container. The image is based upon ubuntu, so we give the command
      “apt-get install -y ping”. Docker will run this command in the container and exit when done.</p>
      """
assignment: """
      <h2>Assignment</h2>
      <p>Install 'ping' inside of the container.</p>
      """
command_expected: ["docker", "run", "learn/tutorial", "apt-get", "install", "-y", "ping"]
result: """<p>That worked!</p>"""
intermediateresults: [
  """<p>Not specifieng -y on the apt-get install command will work for ping, because it has no other dependencies, but
  it will fail when apt-get wants to install dependencies. To get into the habit, please add -y after apt-get.</p>""",
]
tip: """don't forget to use -y for noninteractive mode installation"""
})

q.push ({
html: """
      <h2>Save your changes</h2>
      <p>After you make changes (by running a command inside a container) you probably want to save those changes.
      This will enable you to later start from this point (savepoint) onwards.</p>
      <p>With Docker, the process of saving the state is called <em>committing</em>. Commit basically saves the difference
      between the old image and the new state. The result is a new layer.</p>
      """
assignment: """
      <h2>Assignment</h2>
      <p>First use <em>docker ps -l</em> to find the ID of the container you created by installing ping.</p>
      <p>And then save (commit) this container with the repository name `learn/ping` </p>
      """
command_expected: ["docker", "commit", 'learn/ping']
command_show: ["docker", "commit", "6982a9948422", 'learn/ping']
result: """<p>That worked! Please take note that Docker has returned a new ID. This id is the <em>image id</em>.
        You will need it next.</p>"""
intermediateresults: ["""You have not specified a repository name. This is not wrong, but giving your images a name
                      make them much easier to work with."""]
tip: """<ul>
     <li>Giving just 'docker commit' will show you the possible arguments.</li>
     <li>You don't need to copy the entire ID - as long your input identifies the image. Three or four characters
     is usually enough.</li>
     </ul>"""
})


q.push ({
html: """
      <h2>Run your new image</h2>
      <p>Now you have basically setup a complete, self contained environment with the 'ping' program installed. </p>
      <p>Your image can now be run on any host that runs docker.</p>
      <p>Lets run this image on this machine.</p>
      """
assignment: """
      <h2>Assignment</h2>
      <p>Run the ping program to ping www.google.com</p>

      """
command_expected: ["docker", "run", 'learn/ping', 'ping', 'www.google.com' ]
result: """<p>That worked! Note that normally you can use Ctrl-C to disconnect. The container will keep running. This
        container will disconnect automatically.</p>"""
intermediateresults: ["""You have not specified a repository name. This is not wrong, but giving your images a name
                      make them much easier to work with."""]
tip: """<ul>
     <li>Make sure to use the repository name learn/ping to run ping with</li>
     </ul>"""
})




q.push ({
html: """
      <h2>Check your running image</h2>
      <p>You now have a running container. Let's see what is going on.</p>
      <p>Using <em>docker ps</em> we can see a list of all running containers, and using <em>docker inspect</em>
      we can see all sorts of usefull information about this container.</p>
      """
assignment: """
      <h2>Assignment</h2>
      <p><em>Find the container id</em> of the running container, and then inspect the container using <em>docker inspect</em>.</p>

      """
command_expected: ["docker", "inspect", "efe" ]
result: """<p>Success! Have a look at the output. You can see the ip-address, status and other information.</p>"""
intermediateresults: ["""You have not specified a repository name. This is not wrong, but giving your images a name
                      make them much easier to work with."""]
tip: """<ul>
     <li>Remember you can use a partial match of the image id</li>
     </ul>"""
})



q.push ({
html: """
      <h2>Push the image to the registry</h2>
      <p>Now you have verified that your new application container works as it should, you can share it.</p>
      <p>Docker comes with a complete image sharing service, you can push your image there for yourself and others
      to retrieve.</p>
      """
assignment: """
      <h2>Assignment</h2>
      <p>Push your container image to the repository</p>

      """
command_expected: ["docker", "push"]
command_show: ["docker", "push", "learn/ping"]
result: """<p>Yeah! You are all done!</p>"""
intermediateresults: [""" """]
tip: """<ul>
     <li>Docker images will show you which images are currently on your host</li>
     <li>You can only push images to your own namespace.</li>
     <li>For this tutorial we assume you are already logged in as the 'learn' user..</li>
     </ul>"""
})



q.push ({
html: """
      <h2>Interactive Shell</h2>
      <p>Now, since Docker provides you with the equivalent of a complete operating system you are able to get
      an interactive shell (tty) <em>inside</em> of the container.</p>
      <p>Since we want a prompt in the container, we need to start the shell program in the container. </p>
      <p>You may never have manually started it before, but a popular one typically lives at `/bin/bash`</p>
      """
assignment: """
      <h2>Assignment</h2>
      <p>Your goal is to run the tutorial container you have
      just downloaded and get a shell inside of it.</p>
      """
command_expected: ["docker", "run", "-i", "-t", "learn/tutorial", "/bin/bash"]
result: """<p>Great!! Now you have an interactive terminal</p>"""
intermediateresults: [
  """<p>You seem to be almost there. Did you use <em>-i and -t</em>?</p>""",
  """<p>You've got the arguments right. Did you get the command? Try <em>/bin/bash </em>?</p>"""
  """<p>You have the command right, but the shell exits immediately, before printing anything</p>
      <p>You will need to attach your terminal to the containers' terminal.</p>
  """
  ]
tip: """Start by looking at the results of `docker run`, it shows which arguments exist"""
})





###
  Transform question objects into functions
###

buildfunction = (q) ->
  _q = q
  return ->
    console.debug("function called")

    $('#instructions').hide().fadeIn()
    $('#instructions .text').html(_q.html)
    $('#instructions .assignment').html(_q.assignment)
    $('#tipShownText').html(_q.tip)
    if _q.command_show
      $('#commandShownText').html(_q.command_show.join(' '))
    else
      $('#commandShownText').html(_q.command_expected.join(' '))

    window.immediateCallback = (input, stop) ->
      if stop == true # prevent the next event from happening
        doNotExecute = true
      else
        doNotExecute = false

      if doNotExecute != true
        console.log (input)

        data = { 'type': EVENT_TYPES.command, 'command': input.join(' '), 'result': 'fail' }

        # Was like this:  if not input.switches.containsAllOfThese(_q.arguments)

        if input.containsAllOfTheseParts(_q.command_expected)
          data.result = 'success'

          setTimeout( ( ->
            @webterm.disable()
            $('#buttonNext').focus()
          ), 1000)

          results.set(_q.result)
          console.debug "contains match"
        else
          console.debug("wrong command received")

        # call function to submit data
        logEvent(data)

      else



      return
    window.intermediateResults = (input) ->
#      alert "itermediate received"
      results.set(_q.intermediateresults[input], intermediate=true)
    return


for question in q
  f = buildfunction(question)
  questions.push(f)


# load the first question, or if the url hash is set, use that

###
  Initialization of program
###

if (window.location.hash)
  try
    currentquestion = window.location.hash.split('#')[1].toNumber()
    questions[currentquestion]()
    current_question = currentquestion
  catch err
    questions[0]()
else
  questions[0]()

$('#results').hide()


###
  Event handlers
###


## next
$('#buttonNext').click ->
  next()
  $('#results').hide()

## previous
$('#buttonPrevious').click ->
  previous()
  $('#results').hide()

## submit feedback
$('#feedbackSubmit').click ->
  feedback = $('#feedbackInput').val()
  data = { type: EVENT_TYPES.feedback, feedback: feedback}
  logEvent(data, feedback=true)

## fullsize
$('#fullSizeOpen').click ->
  goFullScreen()

@goFullScreen = () ->
  console.debug("going to fullsize mode")
  $('.togglesize').removeClass('startsize').addClass('fullsize')

  $('.hide-when-small').css({ display: 'inherit' })
  $('.hide-when-full').css({ display: 'none' })

#  $('#overlay').addClass('fullsize')
#  $('#main').addClass('fullsize')
#  $('#tutorialTop').addClass('fullsize')
  webterm.resize()
  data = { type: EVENT_TYPES.start }
  logEvent(data)


## leave fullsize
$('#fullSizeClose').click ->
  leaveFullSizeMode()

leaveFullSizeMode = () ->
  console.debug "leaving full-size mode"

  $('.togglesize').removeClass('fullsize').addClass('startsize')

  $('.hide-when-small').css({ display: 'none' })
  $('.hide-when-full').css({ display: 'inherit' })

#  $('#overlay').removeClass('fullsize')
#  $('#main').removeClass('fullsize')
#  $('#tutorialTop').removeClass('fullsize')
  webterm.resize()

## click on tips
#$('#tips').click () ->
#  if not $('#tipHiddenText').hasClass('hidden')
#    $('#tipHiddenText').addClass("hidden").hide()
#    $('#tipShownText').hide().removeClass("hidden").fadeIn()

## click on tips
$('#command').click () ->
  if not $('#commandHiddenText').hasClass('hidden')
    $('#commandHiddenText').addClass("hidden").hide()
    $('#commandShownText').hide().removeClass("hidden").fadeIn()
