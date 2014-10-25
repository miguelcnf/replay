
from subprocess import check_call

class replay:
    ''' replay wrapper '''

    def run(self, playbook_file, inventory_file):
        ''' hacky syscall to run ansible-playbook '''

        try:
            run_ansible_playbook = 'ansible-playbook -i %s %s' % (inventory_file, playbook_file)
            check_call(['/bin/bash', '-c', run_ansible_playbook])
        except Exception, e:
            raise Exception('Unexpected: %s at module %s' % (e, self.__class__.__name__))
