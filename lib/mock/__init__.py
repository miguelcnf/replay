
import yaml
import time
import random
from os.path import expanduser

class mock:
  ''' mock module '''

  def __init__(self):
    ''' initiates the mock module '''

    random_hash = self.getRandomHash()
    self.vars_file = '/tmp/%s.yml' % str(random_hash)
    random_hash = self.getRandomHash()
    self.playbook_file = '/tmp/%s.yml' % str(random_hash)
    random_hash = self.getRandomHash()
    self.inventory_file = '/tmp/%s.yml' % str(random_hash)

    # debug printing...
    #print "vars_file = %s" % self.vars_file
    #print "playbook_file = %s" % self.playbook_file
    #print "inventory_file = %s" % self.inventory_file


  def getRandomHash(self):
    ''' returns a random hash for tmp files '''

    try:
      return '%s' % hash(time.time()+random.randint(1, 9))
    except Exception, e:
      raise Exception('Unexpected: %s at module %s' % (e, self.__class__.__name__))

  def writeVarsFile(self, hack_mode):
    ''' writes the custom vars to a tmp file '''
    
    try:
      if not hack_mode:
        home = expanduser("~")
      else:
        home = './hacking'
      with open('%s/.replay.yml' % home, 'r') as r:
        run_yaml = yaml.load(r)
      r.close()

      with open(self.vars_file, 'w') as w:
        w.write(yaml.dump(run_yaml))
      w.close()      
    except Exception, e:
      raise Exception('Unexpected: %s at module %s' % (e, self.__class__.__name__))


  def writePlaybook(self, jinja_env):
    ''' writes the custom playbook to a tmp file  '''

    try:
      content_yaml = self.renderPlaybook(jinja_env)
      with open(self.playbook_file, 'w') as w:
        w.write(content_yaml)
      w.close()

      return self.playbook_file
    except Exception, e:
      raise Exception('Unexpected: %s at module %s' % (e, self.__class__.__name__))


  def writeInventoryFile(self):
    ''' writes the custom inventory file to a tmp file  '''

    try:
      with open(self.inventory_file, 'w') as w:
        w.write('localhost ansible_connection=local')
      w.close()

      return self.inventory_file
    except Exception, e:
      raise Exception('Unexpected: %s at module %s' % (e, self.__class__.__name__))


  def renderPlaybook(self, jinja_env):
    ''' renders the custom playbook based on replay.yml '''

    try:
      template = jinja_env.get_template('playbook.yml.j2')
      return template.render(vars_file='%s' % self.vars_file)
    except Exception, e:
      raise Exception('Unexpected: %s at module %s' % (e, self.__class__.__name__))