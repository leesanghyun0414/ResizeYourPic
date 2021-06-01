"use strict";

var PixiManager = /** @class */ (function () {

    function PixiManager(imagePaths, imageIds, backgroundImagePath, basePath) {
        this.width =window.innerWidth > 320 ? window.innerWidth / 320 : window.innerWidth;
        this.height = window.innerWidth > 320 ? window.innerHeight / (window.innerWidth / 320) : window.innerHeight;
        this.canvasId = 'app';
        this.appElement = document.getElementById(this.canvasId);
        this.baseLocationX = this.width / 2;
        this.baseLocationY = this.height / 2;
        this.characterSprites = new Array();
        this.isInteractive = true;
        this.isButtonMode = true;
        this.isDragged = false;
        this.basePath = basePath;
        this.characterIds = imageIds;
        this.characterImagePaths = imagePaths;
        this.characterSprites = this.getSprites(imagePaths); // get sprite array not yet add PIXIjs application.
        this.backgroundSprite = this.getBackgroundSprite(backgroundImagePath);
        this.isWideScreen = innerWidth > innerHeight;
        this.setRadiusAndBaseLocationY();
        this.app = this.getPixiApp();
        this.appendView();
    }

    PixiManager.prototype.setRadiusAndBaseLocationY = function () {
        if (this.isWideScreen) {
            this.r = innerHeight / 2 - innerHeight / 3.6;
            this.baseLocationY -= 40;
        } else {
            this.r = innerWidth / 2 - innerWidth / 3.6;
           this.baseLocationY -= 90;
        }
    };

    PixiManager.prototype.setCharacterSpritesProperty = function () {
        // Find the reference angle according to the number of characterSprites.
        var additionAngle = this.getAdditionAngle();
        var currentAngle = 0;
        // Give the reference coordinates to the first sprite object.
        this.characterSprites[0].y = this.baseLocationY + this.r;
        this.characterSprites[0].x = this.baseLocationX;
        var atan2 = this.getAtan2(this.characterSprites[0]);
        //Set properties of Sprite.
        for (var _i = 0, _a = this.characterSprites; _i < _a.length; _i++) {
            var characterSprite = _a[_i];
            var spriteIndex = this.characterSprites.indexOf(characterSprite);
            var currentRadian = this.getRadian(currentAngle);
            characterSprite.interactive = this.isInteractive;
            characterSprite.buttonMode = this.isButtonMode;
            characterSprite.x = this.baseLocationX + this.r * Math.cos(atan2 + currentRadian) / 0.7;
            characterSprite.y = this.baseLocationY + this.r * Math.sin(atan2 + currentRadian) / 2.2;
            characterSprite.anchor.set(0.5, 0.5);
            this.setZIndex(characterSprite, characterSprite.y);
            this.setScale(characterSprite);
            currentAngle += additionAngle;
            if (characterSprite.name == null) {
                characterSprite.name = this.characterIds[spriteIndex];
            }
            this.addGreyScale(characterSprite);
        }
    };

    PixiManager.prototype.setZIndex = function (sprite, value) {
        sprite.zIndex = value;
    };
    PixiManager.prototype.run = function () {
        this.setCharacterSpritesProperty();
        this.setBackgroundSpriteProperty();
        this.addListenerOnCharacterSprites();
        this.addCharacterSprites();
        this.addBackgroundSprite();
    };

    PixiManager.prototype.setBackgroundSpriteProperty = function () {
        //Set scale.
        this.backgroundSprite.scale.set(1, 1);
this.backgroundSprite.width = this.width;
this.backgroundSprite.height = this.height;
        console.log(this.backgroundSprite.x, this.backgroundSprite.y);
        //Set zIndex always backmost.
        this.setZIndex(this.backgroundSprite, -1);
    };

    PixiManager.prototype.setScale = function (sprite) {

let add = 1.2
        let iner = innerWidth >= 640 ? innerWidth : 640;
        add = innerWidth <= 640 ? add + 0.6 : add;
        if (this.isWideScreen) {

   if (sprite.scale.y <= 1.5 && sprite.scale.x <= 1.5) {
       sprite.scale.set(
           Math.abs(innerWidth / 2 / iner - Math.abs(((this.baseLocationY + this.r) - sprite.y) / iner * add))
           , Math.abs(innerHeight / iner - Math.abs(((this.baseLocationY + this.r) - sprite.y) / iner * add))
       );
   }

        } else {
            if (sprite.scale.y <= 1.5 && sprite.scale.x <= 1.5) {
                sprite.scale.set(
                    Math.abs(innerWidth / iner - (((this.baseLocationY + this.r) - sprite.y) / iner * add))
                    , Math.abs(innerHeight / 2 / iner - (((this.baseLocationY + this.r) - sprite.y) / iner * add))
                );
            }
        }
    };

    PixiManager.prototype.setPosition = function (sprite, radian) {
        sprite.y = this.baseLocationY + this.r * Math.sin(radian) / 2.2;
        sprite.x = this.baseLocationX + this.r * Math.cos(radian) / 0.7;
    };

    PixiManager.prototype.getSprites = function (imagePaths) {
        var spriteObjects = new Array();
        for (var _i = 0, imagePaths_1 = imagePaths; _i < imagePaths_1.length; _i++) {
            var imagePath = imagePaths_1[_i];
            spriteObjects.push(PIXI.Sprite.from(imagePath));
        }
        return spriteObjects;
    };

    PixiManager.prototype.getAdditionAngle = function () {
        return 360 / this.characterSprites.length;
    };

    PixiManager.prototype.getBackgroundSprite = function (imagePath) {
        return PIXI.Sprite.from(imagePath);
    };

    PixiManager.prototype.getAtan2 = function (sprite) {
        return Math.atan2(sprite.y - this.baseLocationY, sprite.x - this.baseLocationX);
    };

    PixiManager.prototype.getRadian = function (angle) {
        return angle * (Math.PI / 180);
    };

    PixiManager.prototype.getPixiApp = function () {
        var pixiApp = new PIXI.Application(// create PIXIjs application.
            {
                width: this.width,
                height: this.height,
                antialias: true,
                resizeTo: window
            });
        pixiApp.stage.sortableChildren = true;
        return pixiApp;
    };

    PixiManager.prototype.sortSprites = function () {
        // First index of character Sprite.
        var firstCharacterSprite = this.characterSprites.filter(function (x) {
            return typeof x !== undefined;
        }).shift();
        switch (true) {
            case (firstCharacterSprite.x < this.baseLocationX): // left swap
                var last = this.characterSprites.pop();
                this.characterSprites.unshift(last);
                break;
            case (firstCharacterSprite.x > this.baseLocationX): // right swap
                var first = this.characterSprites.shift();
                this.characterSprites.push(first);
                break;
            default:
                break;
        }
    };
    /**
     * Add child to stage.
     */
    PixiManager.prototype.addBackgroundSprite = function () {
        this.app.stage.addChild(this.backgroundSprite);
    };
    /**
     * Redraw sprite array
     * @protected
     */
    PixiManager.prototype.reDraw = function () {
        this.sortSprites();
        this.setCharacterSpritesProperty();
    };

    PixiManager.prototype.addGreyScale = function (characterSprite) {
        var isNotFirstCharacter = this.characterSprites.indexOf(characterSprite) !== 0;
        var colorMatrix = new PIXI.filters.ColorMatrixFilter();
        if (isNotFirstCharacter) {
            characterSprite.filters = [colorMatrix];
            colorMatrix.brightness(1.0 - (((this.baseLocationY + this.r) - characterSprite.y) / 1000), false);
        } else {
            characterSprite.filters = [colorMatrix];
            colorMatrix.brightness(1.0, false);
        }
    };

    PixiManager.prototype.addListenerOnCharacterSprites = function () {
        var _this = this;
        for (var _i = 0, _a = this.characterSprites; _i < _a.length; _i++) {
            var sprite = _a[_i];
            sprite
                .on('pointerdown', function (e) {
                    return _this.onClick(e);
                })
                .on('pointerup', function (e) {
                    return _this.endMove(e);
                });
        }
    };

    PixiManager.prototype.onClick = function (e) {
        var _this = this;
        console.log("Is clicked");
        e.target.on('pointermove', function (e) {
            return _this.onMove(e);
        });
    };

    PixiManager.prototype.onMove = function (e) {
        this.isDragged = true;
        //Event firing coordinates.
        var picLocalPosition = e.data.getLocalPosition(this.app.stage);
        //Atan2 of event firing coordinates between base coordinates.
        var localPositionAtan2 = this.getAtan2(picLocalPosition);
        //Update Sprite properties.
        this.updateSpriteProperties(localPositionAtan2);
    };
    /**
     * Method called while moving the pointer.
     * Update properties of Sprite.
     * @param currentRadian Latest radians moving pointer.
     * @protected
     */
    PixiManager.prototype.updateSpriteProperties = function (currentRadian) {
        for (var _i = 0, _a = this.characterSprites; _i < _a.length; _i++) {
            var sprite = _a[_i];
            // Angle that corresponds to the order of sprite.
            var positionDegree = (360 / this.characterSprites.length) * this.characterSprites.indexOf(sprite);
            var spriteRadian = positionDegree * (Math.PI / 180);
            var radian = currentRadian + spriteRadian;
            this.setPosition(sprite, radian);
            this.setZIndex(sprite, sprite.y);
            this.setScale(sprite);
        }
    };
    /**
     * Processing when the pointer is removed.
     * Dragged
     * @param e Event data of Sprite.
     * @protected
     */
    PixiManager.prototype.endMove = function (e) {
        //If the onMove event has not fired, move to the link destination.
        if (this.isDragged == false) {
            location.href = this.basePath + e.target.name;
        } else {
            this.isDragged = false;
        }
        this.characterSprites[0].removeListener("pointermove", this.onMove);
        this.reDraw(); // Redraw character Sprite.
    };
    /**
     * Add Sprites on PIXI Application stage.
     * @public
     */
    PixiManager.prototype.addCharacterSprites = function () {
        for (var _i = 0, _a = this.characterSprites; _i < _a.length; _i++) {
            var sprite = _a[_i];
            this.app.stage.addChild(sprite);
        }
    };
    /**
     * Append PIXI Application to HTMLElement.
     * @protected
     */
    PixiManager.prototype.appendView = function () {
        this.appElement.appendChild(this.app.view);
    };
    return PixiManager;
}());

