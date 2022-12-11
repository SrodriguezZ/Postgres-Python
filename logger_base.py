import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('CAPA_DE_ERRORES'),
                    log.StreamHandler()
                ])
if __name__=='__main__':
    log.debug('MENSAJE DEBUG')
    log.info('MENSAJE INFORMATIVO')
    log.warning('MENSAJE WARNING')
    log.error('MENSAJE ERROR')
    log.critical('MENSAJE CRITICO')