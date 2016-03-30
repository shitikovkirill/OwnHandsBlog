<?php
// bootstrap.php
require_once "vendor/autoload.php";
use Doctrine\ORM\Tools\Setup;
use Doctrine\ORM\EntityManager;

class Doctrine{
    private $entityManager;
    protected static $_instance;

    private function __construct(){
        if(!defined ('DB_HOST')){
            require_once '../../../wp-config.php';
        }
        $paths = array(__DIR__."/entity");
        $isDevMode = true;

        // the connection configuration
        $dbParams = array(
            'driver'   => 'pdo_mysql',
            'hostname' => DB_HOST,
            'user'     => DB_USER,
            'password' => DB_PASSWORD,
            'dbname'   => DB_NAME,
        );

        $config = Setup::createAnnotationMetadataConfiguration($paths, $isDevMode);
        $this ->entityManager = EntityManager::create($dbParams, $config);
    }

    private function __clone(){
    }

    public static function getInstance() {
        if (null === self::$_instance) {
            self::$_instance = new self();
        }
        return self::$_instance;
    }

    public function getEntityManager (){
        return $this->entityManager;
    }
}
