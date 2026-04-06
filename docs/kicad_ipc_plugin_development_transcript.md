# Transcript: KiCad IPC Plugin Development by Otto Strydom @KiCon 2024

[00:00:04] Thank you. Can you hear the back? Okay.

[00:00:09] Louder.

[00:00:12] And you're out. Welcome. Uh I'm really

[00:00:16] uh embedded software developer. So I

[00:00:19] think most of you have may experience in

[00:00:22] me in key cat. are uh asking pretty much

[00:00:26] about Keycat and uh yeah the new

[00:00:29] interface to the plugins.

[00:00:33] I just wash your hands. How many of you

[00:00:35] have got plugging for Gout?

[00:00:42] We not here. Okay.

[00:00:46] Yeah. So, and uh anyone try the new IPC

[00:00:51] plug-in interface? Yeah. Okay. So, one

[00:00:55] there. Yeah. I'm not going to go into

[00:00:58] why do you need plugins, but uh

[00:01:02] I'm first going to sort of look have a

[00:01:04] very quick look between old and the new

[00:01:06] interface. What does it look like and

[00:01:09] what's the difference? And then I'm

[00:01:11] going to look at the architecture of the

[00:01:13] new interface because that is really a

[00:01:15] big shift from the old to the new. when

[00:01:19] I'll be brave and have a demo. I think

[00:01:22] everyone's avoided having a demo up the

[00:01:26] list,

[00:01:27] but I will both and then uh I'll sort of

[00:01:31] go in reverse and have a demo first and

[00:01:33] then look at the code and then look at

[00:01:36] how to get started. So, I'll try and do

[00:01:38] the interesting stuff in the beginning.

[00:01:41] Uh I'll try to make it very short 20

[00:01:44] minutes or so and then we can have some

[00:01:46] time for questions.

[00:01:48] So

[00:01:50] yeah

[00:01:52] first of all the old interface the old

[00:01:55] interface if you look at it from a

[00:01:57] technical point of view was really a

[00:01:59] direct call on wall plugging to into the

[00:02:03] code itself. So this was a very close

[00:02:06] tight connection and that is why on a

[00:02:10] lot of versions when you change the

[00:02:11] version it actually broke the interface

[00:02:14] because this was closer to their actual

[00:02:18] code and once they changed the code the

[00:02:20] interface actually changed.

[00:02:23] So uh and they ported Python.

[00:02:27] So with the mule interface they really

[00:02:29] split

[00:02:31] like a big split between the application

[00:02:34] geat and the plugin. Okay. So these were

[00:02:38] really two independent

[00:02:40] applications running now and then they

[00:02:43] communicate with each other using

[00:02:44] sockets or this communication is MNG and

[00:02:48] protobuff. I'm not going to go into

[00:02:50] exactly at ease,

[00:02:53] but each one of these actually are

[00:02:56] running an environment. So if you looked

[00:02:58] at the old API,

[00:03:02] they ran a custom Python interpreter

[00:03:07] inside Kcad actually. So every time they

[00:03:10] release key CAD I compile a Tyson Tyson

[00:03:13] version per keycat the new one it will

[00:03:18] be completely separate. So if you run

[00:03:20] your

[00:03:22] plugin this will actually run your

[00:03:27] system.

[00:03:28] Okay. So there is a little bit of

[00:03:31] responsibility to the user now where we

[00:03:33] have to install their own button. So

[00:03:37] because this is entertainment curses, it

[00:03:40] actually gives people the opportunity to

[00:03:43] write plugins in other languages as

[00:03:46] well, which I think is important.

[00:03:48] Obviously, I'll stick with Python.

[00:03:52] So this is just sort of a very

[00:03:55] simplified way of representing how we

[00:03:58] need and it's going to work where you

[00:04:00] have your kick out on the one side and

[00:04:03] you have your plugin in one side and

[00:04:06] then you basically send messages using

[00:04:09] uh your sockets in your application. So

[00:04:15] I'll start off with the demo.

[00:04:19] So you will see that uh

[00:04:24] don't know this is a very simple hello

[00:04:27] world demo. Okay. So the only thing it's

[00:04:30] going to do is it's going to place a

[00:04:32] hello world on the PCB

[00:04:40] if I can find the mouse. So when you

[00:04:43] install a plugin, you actually get the

[00:04:46] new icon. In this case, this is just the

[00:04:51] icon. And when I place it, you should

[00:04:54] see text somewhere around there. I hope

[00:04:59] it doesn't because it placed it out of

[00:05:02] screen.

[00:05:03] Yeah. But uh with me move this.

[00:05:08] So I'm going to move this. And when I

[00:05:11] test it again, it should price emperor

[00:05:15] alleg.

[00:05:18] And there it is. Okay. So this is just

[00:05:21] very simple.

[00:05:26] So let's look at what do you need to do

[00:05:28] this.

[00:05:31] So

[00:05:34] the best thing when you work in Python

[00:05:37] is you have to input what you need and

[00:05:40] you might have to import some additional

[00:05:43] components. In the case of a plug-in you

[00:05:46] import key.

[00:05:49] So the fifth step will be to actually

[00:05:51] insp is this connection to key cat and

[00:05:55] for that it's just simple do a all to

[00:05:58] key card and you get a reference to it

[00:06:01] and once you have a reference to keycat

[00:06:03] you must get access to a PCB in keycard

[00:06:08] okay so one thing that I didn't mention

[00:06:11] is you must have keycat open so you if

[00:06:16] you don't have keycat open this will

[00:06:18] file

[00:06:23] The next thing you want is you want to

[00:06:25] get some information on your PCD. So it

[00:06:31] depends really on what you want to do.

[00:06:33] In most cases, I think you might want to

[00:06:37] manipulate your PCB components. So to do

[00:06:40] that you do a call to get preprints but

[00:06:44] you might also want to do some other

[00:06:46] things while for example getting the

[00:06:48] tracks getting the m all that is

[00:06:51] selected and for each one of those you

[00:06:53] have a different way.

[00:06:58] So once you have access to these

[00:07:00] components, you can loop over them in

[00:07:03] this case and I'll quickly show if you

[00:07:06] want to extract some information on

[00:07:08] these components.

[00:07:11] So I've written a small frequent

[00:07:15] function and this was simply

[00:07:18] printed reference field text value which

[00:07:22] is your references that we used to like

[00:07:25] R1 or I see one or whatever somebody was

[00:07:30] assigned to a component and then you can

[00:07:34] look at for example

[00:07:36] the position

[00:07:38] or which layer array is on. Okay, so

[00:07:41] this is just extracting information.

[00:07:46] Uh you can also look at the paths

[00:07:49] because you have multiple paths on each

[00:07:51] reprint.

[00:07:53] So yeah, I'm just going to quickly go

[00:07:56] through this. You can go pad by pad. We

[00:07:59] can look at the type, the position.

[00:08:04] >> This aren't told that.

[00:08:08] >> Uh

[00:08:10] now you can go ahead and you can

[00:08:12] actually change this position of your

[00:08:15] component and fold out this bolt in

[00:08:19] uh vector two, which is just the X and

[00:08:22] the Y position really. And you can

[00:08:25] assign this footprint position to the

[00:08:30] new position.

[00:08:32] What is uh interesting about the

[00:08:36] coordinate system in KCAD is that it's

[00:08:40] not what we used to. The top left is

[00:08:44] actually position zero. So that Y as

[00:08:47] there is down. Okay. I know in the new

[00:08:51] Keycad you can save it in your options

[00:08:54] or it's still going to be in reverse

[00:08:59] in your API

[00:09:02] queries. Okay, so

[00:09:05] that's just a little bit confusing at

[00:09:07] beginning but you get used to it. Also

[00:09:10] the model means in nanometers so if you

[00:09:14] want to use different units you have to

[00:09:16] do a conversion. B is both in conversion

[00:09:20] for millime to CQ1 is mmters.

[00:09:25] The above thing that's important is to

[00:09:29] back the different levels.

[00:09:32] So internally the layers are really

[00:09:34] numbers and they've conveniently

[00:09:38] supplied inated parts for the different

[00:09:42] lowers. in those scales. In this example

[00:09:45] is basically port lower front selfcreen

[00:09:50] and port lower packed copper. Again

[00:09:58] uh similarly to passing something we can

[00:10:00] move it but I overlay the plus equals

[00:10:03] operator. Say you just give the the

[00:10:06] things that you want to move it and

[00:10:08] assign it to the position

[00:10:13] or you can add something like that in

[00:10:16] theory.

[00:10:18] Uh so you can import whatever component

[00:10:23] or item you want to add. In this case,

[00:10:26] broad text. You create it

[00:10:30] with the B text function call or you

[00:10:34] could do something like adding a track

[00:10:37] by creating a new track.

[00:10:42] Uh so once you've created this item, you

[00:10:46] actually want to set up some parameters

[00:10:49] for it. In this case, hello Kyad plugin.

[00:10:54] In the text field, uh you want to set

[00:10:57] the position which is you can see in

[00:11:01] millimeters in this case and you want to

[00:11:05] set up which port level we want to lose.

[00:11:08] So screen

[00:11:10] will loot can set up tracks with

[00:11:14] starting positions and so on.

[00:11:17] So once you've actually

[00:11:21] created or changed your components, you

[00:11:24] want to connect this to KCAD. Okay. And

[00:11:27] the way that KCAD does this is similar

[00:11:30] to G vision control. We will have a uh

[00:11:36] commit and you actually do a push of

[00:11:39] your commit. Right? So

[00:11:43] they

[00:11:44] set up your commit

[00:11:47] you will

[00:11:49] give it a list of all the changes action

[00:11:52] of all the components you have uh

[00:11:54] created in this case and then you do a

[00:12:00] push commit to actually send it through

[00:12:03] to key. Okay,

[00:12:06] so this is if you created components and

[00:12:09] slightly different if you have modified

[00:12:13] components and the reason for that is is

[00:12:16] that it should actually match up your

[00:12:18] changes to what's in parallel. Okay. So

[00:12:22] in that case you also be a beginning

[00:12:24] commit

[00:12:26] but you don't do a create items you do

[00:12:29] an update items and then once again you

[00:12:33] do a push commit.

[00:12:36] So one thing that's interesting is that

[00:12:40] you could actually have multiple steps

[00:12:42] that you do in a commit all at the same

[00:12:45] time. Okay. How it influences the user

[00:12:49] on the Wizer side is this. This will all

[00:12:52] be combined into one undo. So whatever

[00:12:55] you do in plugin

[00:12:58] the louver can actually undo with

[00:13:01] contraet whatever key are using for

[00:13:04] that. Okay. But it also means that you

[00:13:07] can split up your operations into

[00:13:11] multiple undo steps. Though in some

[00:13:14] cases it might be convenient if the

[00:13:16] wizard can test through certain steps

[00:13:19] and undo them one at a time.

[00:13:28] This is simply steps combined. So with

[00:13:32] these string commands you can actually

[00:13:34] add something on your board.

[00:13:40] So um if I want to summarize the flow,

[00:13:43] you basically do a setup which is

[00:13:46] getting a reference to your kickart and

[00:13:49] getting a reference to the PCB. You do

[00:13:54] your operations, your business logic as

[00:13:56] the software people call it and what you

[00:13:58] want to do on the PCB and then you

[00:14:01] commit them.

[00:14:05] So, uh, I'm quickly going to try another

[00:14:09] DL.

[00:14:14] And this one is really just the code

[00:14:18] that I've shown earlier. They are just

[00:14:20] print out information of the components

[00:14:24] on the PCB. Okay. So, this is not going

[00:14:26] to do anything on the PCB. What I am

[00:14:30] also showing in this case is the

[00:14:31] previous one I ran the plugin directly

[00:14:34] from Kcad. In this case I'm actually

[00:14:38] running it as a separate process in a

[00:14:42] terminal. Okay.

[00:14:44] So you have the different options. You

[00:14:47] can run your plug-in from within keycard

[00:14:50] but you can also run it completely

[00:14:52] separately.

[00:14:57] So this one will simply print out a list

[00:14:59] of what's going on with the components.

[00:15:06] Scroll up a bit. So what you will see is

[00:15:11] value one. Sorry. it have how many pads

[00:15:14] it's got

[00:15:16] the

[00:15:18] of the mate connected to this pad the

[00:15:21] type of the pad and this is if it's

[00:15:24] through or SMV or something like that uh

[00:15:27] the position offset size and turn each

[00:15:31] each pad

[00:15:33] and you can also see on which layer it

[00:15:37] is so you can get information from

[00:15:42] exactly what uh is in it but this is

[00:15:45] just for

[00:15:48] instruction really.

[00:15:54] Yeah. So that masiki computes the Python

[00:15:59] side of it. Now how do you actually get

[00:16:03] this into our into keycat into

[00:16:07] application itself?

[00:16:09] Well, for installation it actually for

[00:16:14] you need through a four files depending

[00:16:18] on what it is. For Python you need four

[00:16:20] fires and before you do anything you

[00:16:24] have to do instead of your uh package

[00:16:29] that you want to use which is Gat

[00:16:32] Python.

[00:16:34] And if you ask the AI about it, it gets

[00:16:37] very confused because the package name

[00:16:41] and what you import is different. Okay?

[00:16:44] So be aware the install is key python

[00:16:48] while the import is key.

[00:16:53] The

[00:16:54] then you can use any development

[00:16:58] environment you

[00:17:00] really comfortable with in python. So

[00:17:02] you can use PyCharm or ReX code or uh

[00:17:07] command line. So you have a lot of

[00:17:09] flexibility in your development

[00:17:11] environment.

[00:17:13] Uh yeah once again wrote it requires key

[00:17:17] PCB to be open. Okay.

[00:17:23] So to do a install of this plug-in you

[00:17:26] need a PIS mention these files are

[00:17:30] plugin.json JSON and this is a JSON par

[00:17:33] that specifies

[00:17:35] to KCAT what is actually going on. I'll

[00:17:40] look at it in a little bit more detail.

[00:17:43] >> Uh you have your application files which

[00:17:47] is your Python files and in those cases

[00:17:50] you want an icon that's on the top right

[00:17:53] in the example.

[00:17:56] So these files you basically copy all

[00:17:59] three of them. There's a false line that

[00:18:01] I'll target just now.

[00:18:03] But you copy this into the gard pluging

[00:18:07] fer. This fer is different for different

[00:18:11] platforms. This is for Linux.

[00:18:16] Uh you have the unique plug-in name. So

[00:18:20] you inside this local shares Kycat

[00:18:23] plugins you generate you actually create

[00:18:26] a new folder. Okay. So al pass should be

[00:18:30] in this folder. If you have to restart

[00:18:33] keycat

[00:18:35] and kcat is basically when it starts up

[00:18:39] it will check in that folder if there is

[00:18:44] a new file and it will install it for

[00:18:46] you. Okay. So uh

[00:18:50] it tells linkly

[00:18:53] if it fails it doesn't say anything.

[00:18:55] Okay. So you have not have to debug it

[00:19:01] uh which I'll get to later

[00:19:04] but this is a typical

[00:19:08] uh parts that you need for your opinion.

[00:19:12] There's one that I didn't mention and

[00:19:14] that's the requirements that takes file

[00:19:17] and ones that develop with Python knows

[00:19:21] that normally you put your packages that

[00:19:23] you can use in there.

[00:19:29] So in your ping that JSON

[00:19:32] you have to sort of fill in

[00:19:36] give the information to key charact.

[00:19:45] You must also give it a unique

[00:19:47] identifier but it can be anything as far

[00:19:51] as I know anyway.

[00:19:53] You must specify the amp time for Python

[00:19:57] repo always be Python

[00:20:01] and then actions. So actions is what

[00:20:04] buttons you want on the screen and all

[00:20:08] the button you must give it a name. You

[00:20:11] must give it the scope and the scope in

[00:20:14] Scos defines if it's in the PCB or in

[00:20:16] the E schematic. Okay. Uh at this point

[00:20:20] only PCB is supported. So it will always

[00:20:22] be PCB

[00:20:25] and you specify an entry brand and the

[00:20:27] entry point is the file name

[00:20:30] and script

[00:20:33] and lastly just an icon two icons

[00:20:37] actually but they can be the same.

[00:20:42] So um if you want to travel this is

[00:20:47] uh the magic key I've had you basically

[00:20:51] tell on into a tail you set up these

[00:20:54] environment variables which tells Kikat

[00:20:56] to print out more debug information and

[00:20:59] you run kit.

[00:21:03] Yeah. Yeah. I'm slowly running out of

[00:21:06] time. about if you want your own user

[00:21:08] interface, you can really use any user

[00:21:11] interface uh Python user interface you

[00:21:14] want. You can use KT or in most cases uh

[00:21:18] WS windows which is what um KAT's using.

[00:21:24] There are some limitations

[00:21:26] as I said it's PCB only. So only for the

[00:21:29] PCB error current not for schematic yet

[00:21:33] the PCB must be open is a CLI interface

[00:21:38] a command line interface that they're

[00:21:39] working out or you must enable the IPC

[00:21:44] explicitly that's an interesting one. So

[00:21:48] you cannot use the new plins by default

[00:21:53] in version 9. You have to enable it in

[00:21:56] the options.

[00:21:58] And then it must be Python 3.9 to 3.12.

[00:22:02] And obviously it's still a work in

[00:22:04] progress. So you can expect some

[00:22:07] problems.

[00:22:08] Uh yeah. Where's dinner?

[00:22:13] So what I'm going to do in this demo is

[00:22:15] basically place the components and move

[00:22:19] around a little bit.

[00:22:37] So I'm also going to show

[00:22:40] how you can do development.

[00:22:44] So I'm using ES gold and this is my

[00:22:51] Python code.

[00:22:53] So I have placed the broadband

[00:22:57] in my cult and when I'm just going to

[00:23:00] run it interactively in the debugger.

[00:23:11] So where I hit the buy point now I can

[00:23:14] step into

[00:23:18] Wii

[00:23:19] v you will see getting the reference to

[00:23:24] uh Kcat

[00:23:30] there

[00:23:33] and then sorry get the broad from Katak

[00:23:36] and then I'm going to do some operations

[00:23:38] in the background. I'm not going to talk

[00:23:40] through limbs step by step.

[00:23:44] So now that routine has moved the

[00:23:47] components around these components. As

[00:23:49] you see, I'm basically just going to

[00:23:51] rearrange them. Okay.

[00:23:58] So there I do my beginning commit.

[00:24:02] I'll place them.

[00:24:04] And now when I do the update, it should

[00:24:08] update them. And once I do the collect,

[00:24:11] you should see these components should

[00:24:14] rearranged

[00:24:17] somewhere. It's rearranged.

[00:24:21] Okay. So

[00:24:22] that's it basically

[00:24:26] uh

[00:24:28] as far as

[00:24:31] the way central plugin development wise

[00:24:36] that's the QR code for the G repository

[00:24:43] for examples and for the presentation.

[00:24:48] Say yes. That's it.

[00:25:00] >> I can go.

[00:25:07] >> So, uh, thanks for the great talk. Um,

[00:25:10] does Keycad create a virtual environment

[00:25:12] for each, uh, growing

[00:25:15] and install the requirements

[00:25:17] automatically?

[00:25:19] Yeah. Okay. I'm also not sure about the

[00:25:22] answer and I've actually asked Wayne

[00:25:25] about it years ago. So,

[00:25:28] um I don't know if you understand the

[00:25:30] question. He's basically asking me have

[00:25:32] multiple plugins. Do they have their own

[00:25:35] individual environment or if it's like

[00:25:38] in one will they share the same

[00:25:40] environment? Okay. Did I understand it

[00:25:42] correctly? So the answer is that as I

[00:25:47] understand it at this point anyways that

[00:25:49] are really independent from each other.

[00:25:52] So in theory you can actually run two or

[00:25:55] three Python uh plugins and they will

[00:25:59] each have their own virtual environment.

[00:26:02] Okay. So you can actually run different

[00:26:06] versions of Python

[00:26:10] for different for different plugins that

[00:26:13] you have. Okay, this is very tricky to

[00:26:15] do. I can tell you that as well because

[00:26:19] you have the user is now responsible for

[00:26:23] installing the different uh Python

[00:26:26] plugins uh Python versions sorry. Okay.

[00:26:30] So less it is possible. I don't know if

[00:26:32] it's that practical. Yeah.

[00:26:35] >> Yes. Um the the new app is genius. So um

[00:26:41] nice that we have that. Um but I have a

[00:26:44] few drawbacks. One large drawback is if

[00:26:48] I supply

[00:26:50] um plugin by the plug-in manager and the

[00:26:53] API is not activated, I the user see

[00:26:57] nothing. Um, if there exists some hacky

[00:27:01] way to told the user here, uh, it is not

[00:27:05] working, you can't install it

[00:27:09] because it doesn't do anything.

[00:27:12] >> Uh, 100% accurate.

[00:27:16] >> Um, could I ask another question? Um,

[00:27:20] >> let me just finish as well as if it's

[00:27:22] okay. Can I just answer one? Yeah, sure.

[00:27:26] Yeah. So

[00:27:28] uh if I rephrase the question slightly

[00:27:31] is if you want a new plugin

[00:27:34] it basically just nothing it just does

[00:27:38] the user doesn't see anything so if you

[00:27:40] give it to the user he eventually

[00:27:42] nothing happens okay and he doesn't know

[00:27:45] why it's very frustrating and the reason

[00:27:49] why is as I said earli

[00:27:54] explicitly in the settings. I understand

[00:27:56] your question correctly. Okay. So, I

[00:28:00] understand them. I haven't tested this

[00:28:02] yet, but in the latest release 9.04,

[00:28:08] I think it's already enabled, but it's

[00:28:11] definitely going to come in the newer

[00:28:14] releases that if you try to run a new

[00:28:19] plugin, it will tell you that the option

[00:28:21] is not set.

[00:28:23] So,

[00:28:25] troll you is just going to follow the

[00:28:27] user but it's not set

[00:28:29] >> that is also nice because uh currently

[00:28:31] situation is that the user see nothing

[00:28:33] until uh the code is broken uh yeah you

[00:28:38] don't become any messages also if you

[00:28:41] start it over the um terminal the other

[00:28:44] part is what I have a problem is um with

[00:28:48] the graphical user interface it makes

[00:28:50] more fun yeah definitely but um these

[00:28:54] inst instances are separated from kat

[00:28:58] and in principle you can start the um a

[00:29:03] graphical user interface as often if you

[00:29:06] would like. So uh natively there is no

[00:29:09] support that you see there exist an open

[00:29:13] graphical user interface or open

[00:29:15] connection. Is it somewhat how possible

[00:29:19] to see the open IPC connections or could

[00:29:22] it be possible that would be extremely

[00:29:25] helpful?

[00:29:26] >> I I can understand I'll agree with you

[00:29:29] but I don't think so.

[00:29:32] Sorry. What he

[00:29:36] is asking if

[00:29:40] there is a background plugin roaming it

[00:29:43] can be hidden from the user. Correct. Is

[00:29:46] yeah it will can be hidden can either be

[00:29:49] in the background or even it is con's

[00:29:52] own user interface. this might be hidden

[00:29:55] behind the screen and the user doesn't

[00:29:58] know what's going on. And I think this

[00:30:02] question has been asked before on the

[00:30:06] forum

[00:30:08] and nobody really had an answer for how

[00:30:12] yeah how this should be handled but it

[00:30:15] is a definitely a problem. Yeah, what I

[00:30:18] have done is our own IPC server to find

[00:30:20] my instance and that's not so nice. Who

[00:30:24] has so we run a a process check in the

[00:30:28] background as it's

[00:30:32] blinded but it's

[00:30:35] but it's awkward.

[00:30:38] >> Yes. Yeah. Hi. So what happens if you

[00:30:42] don't follow the proper commit protocol?

[00:30:45] So like you send an update command

[00:30:47] without having created a commit or you

[00:30:51] exit before you commit the commit or you

[00:30:55] begin a commit that you don't like uh

[00:31:00] push and then you begin another one.

[00:31:04] >> Okay. Yeah. So if you so because it's

[00:31:07] already two independent processes

[00:31:10] now I'm guessing a little bit but I mean

[00:31:12] the commit was like a get commit for

[00:31:16] really the same idea. Uh so the actual

[00:31:20] data will only be sent when you do the

[00:31:24] commit. So if you don't do a commit

[00:31:28] nothing is going to happen.

[00:31:30] that there is one thing that I did not

[00:31:33] mention. When you do the updates, it

[00:31:37] will actually return a list of

[00:31:41] compilements or actions whatever you

[00:31:44] want to call it. And this might not

[00:31:47] actually match what you have committed.

[00:31:52] Okay? And the reason why is if you look

[00:31:55] at this at the ball lower technical

[00:31:58] level

[00:32:00] within Kyad they have the event Q. Okay,

[00:32:04] this event Q all events and that

[00:32:07] includes user events and I think it also

[00:32:10] includes events between the PCB and the

[00:32:14] schematic. Okay, it all goes into this

[00:32:17] event Q and this event Q then execute

[00:32:22] whatever is in the queue. Okay, and the

[00:32:25] reason for this is to keep consistency

[00:32:27] between in the data structure. So in

[00:32:31] this case you might ask it for the

[00:32:34] components and someone might go and

[00:32:37] actually delete some of those components

[00:32:39] in the background while you sort of

[00:32:41] manipulating them on the one side or

[00:32:44] when you commit them that components

[00:32:47] gone. Okay. And that is why when you get

[00:32:50] a return it might not be all

[00:32:54] components in it anymore. So

[00:32:56] >> in theory you should very fine but I

[00:32:59] think most people are not going to worry

[00:33:00] about it too much

[00:33:03] >> if you

[00:33:05] don't spoke anyone working on the PCB to

[00:33:08] go something in the background.

[00:33:13] >> Um my question is concerning the board.

[00:33:16] You told us that at the moment only the

[00:33:19] board is supported for plugins. Are

[00:33:21] there any plans to include the shatics

[00:33:24] for plugins?

[00:33:26] turning on you supporting schematic.

[00:33:29] >> Yes, that that I could do could do maybe

[00:33:32] um

[00:33:33] create a plug-in for the chatic side.

[00:33:41] >> Yeah, I know you all are planning and I

[00:33:44] think Wayne said it yesterday as well.

[00:33:47] They are planning but

[00:33:50] if you look back in history this has

[00:33:53] been planned for at least six years.

[00:34:01] So I won't know what is going to happen,

[00:34:03] but I think that they actually will do

[00:34:07] it eventually because

[00:34:09] there's definitely value in this because

[00:34:12] there's some information in the

[00:34:13] schematic that you don't have in the

[00:34:15] PCB. Okay. Or like if it's

[00:34:21] differential pair for example. I don't

[00:34:23] know if that's I don't think it's

[00:34:25] available in the PCB. You have to get it

[00:34:27] from the fanatic information. So it was

[00:34:31] definitely me myself I would like to see

[00:34:34] in which uh hello gear it is which and

[00:34:39] at this point I can't get it. So yeah

[00:34:42] it's totally supported.

[00:34:46] >> We have one question about the

[00:34:48] requirement. Do um the package are

[00:34:51] installed when kad is launched? I I I

[00:34:55] mean um um you have some requirements

[00:34:59] and uh if they are not installed in the

[00:35:02] system uh do the plane does not work or

[00:35:06] say an error

[00:35:08] >> in in the requirements.ext file

[00:35:11] for Python what packages you need to

[00:35:13] say.

[00:35:14] >> Yes. Yes. So uh so if you're using

[00:35:18] packages in Python it must be in the

[00:35:21] requirements file and as I said earlier

[00:35:24] unfortunately

[00:35:26] it fails silently at this point. So if

[00:35:30] you don't have it in the requirements

[00:35:33] it's just going to fail and it's not

[00:35:35] going to give you any feedback on it and

[00:35:38] hopefully they will

[00:35:44] ah Right.

[00:35:59] >> Yes. Yes.

[00:36:01] >> I don't know exactly what time it's

[00:36:03] live. I think it's live when it starts

[00:36:07] up, but I am not sure. I don't know if

[00:36:10] anyone else

[00:36:17] Oh, you

[00:36:19] >> okay? Okay. So, TSI

[00:36:24] Nice.

[00:36:26] >> Um, do you know if it's possible to use

[00:36:27] the uh IPC uh API to um raise DRC errors

[00:36:32] or warnings and maybe place DRC flags?

[00:36:36] >> Well, I was wondering about it as well.

[00:36:40] As far as I know,

[00:36:44] not really,

[00:36:46] but obviously you can write uh

[00:36:52] if you want to do it as a separate step

[00:36:54] and trying to plug into this unexpected

[00:37:04] from your PCB and then write your own

[00:37:07] Python code to actually calculate

[00:37:10] the senses. But I think it's a little

[00:37:13] awkward to deal with. Yeah. And it also

[00:37:16] means that he's not going to go into

[00:37:18] your

[00:37:19] errors because you actually want it all

[00:37:23] to be in the same place. So yeah,

[00:37:28] I think these things make a lot of sense

[00:37:32] because I said also thought about it. I

[00:37:34] think they're probably going to add it

[00:37:36] as time goes by that you can actually

[00:37:39] add, you know, feed something back into

[00:37:43] editor.

[00:37:47] anymore.

[00:37:54] >> Sorry, I just

[00:37:58] uh

[00:38:00] you you have a command to make a DSC in

[00:38:03] the terminal and then you can combinate

[00:38:05] it with the IPC interface.

[00:38:10] >> So that's definitely possible.

[00:38:13] >> Okay. But but you do through command

[00:38:16] line correct okay I didn't know that

[00:38:22] okay thank you everyone