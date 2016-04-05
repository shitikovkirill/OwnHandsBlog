<?php
// bootstrap.php
namespace Doctrine;

require_once "vendor/autoload.php";

use Doctrine\ORM\Tools\Setup;
use Doctrine\ORM\EntityManager;

class Doctrine{
    private $entityManager;
    protected static $_instance;

    private function __construct(){

        $paths = array(__DIR__."/entity");
        $isDevMode = true;

        $dbParams = array(
            'driver'   => 'pdo_mysql',
            'hostname' => 'localhost',
            'user'     => 'root',
            'password' => '',
            'dbname'   => 'wp_superliv_no',
        );
        if(defined ('DB_HOST')){
            // the connection configuration
            $dbParams = array(
                'driver'   => 'pdo_mysql',
                'hostname' => DB_HOST,
                'user'     => DB_USER,
                'password' => DB_PASSWORD,
                'dbname'   => DB_NAME,
                'charset'   =>'utf8'
            );
        }

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
