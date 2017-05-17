# docparser (.py)
# SourceDocs ver1.0.0.
# Developed by Louis Ronald, Ronsoft Technologies.
# (C) 2017. All Rights Reserved.

# this parser is the super class of all parsers used in the SourceDocs
# project. Methods and attributes in here are essentially inherited by
# all other sub-classes. All tags and keys delcared in this class are
# universally applicable to source codes in virtually all programming
# languages. :-)

class docparser:
    
    ''' docparser class '''

    ############################################################
    ##  declaration of generic SourceTag documentation tags   ##
    ############################################################

    ''' source-file-specific tags '''
    TAG_FILE =                      "@file"
    TAG_CONTRIBUTOR =               "@contributor"


    ''' class-specific tags '''
    TAG_CLASS =                     "@class "
    TAG_CLASS_ATTRIBUTE =           "@class-attr "

    ''' class-method specific tags '''
    TAG_CLASS_METHOD =              "@class-method "
    TAG_CLASS_METHOD_PARAM =        "@class-method-param "
    TAG_CLASS_METHOD_RETURN =       "@class-method-return "

    ''' non-class method tags '''
    TAG_METHOD =                    "@method "
    TAG_METHOD_PARAM =              "@method-param "
    TAG_METHOD_RETURN =             "@method-return "

    ''' non-class attribute tags '''
    TAG_ATTRIBUTE =                 "@attr "


    ############################################################
    ##    declaration of standard data keys for tag data      ##
    ############################################################

    KEY_NAME =                      'name'
    KEY_VISIBILITY =                'vis'
    KEY_DESCRIPTION =               'descr'
    KEY_EXTENDS =                   'extends'
    KEY_DATATYPE =                  'type'
    KEY_IMMUTABLE =                 'imm'

    KEY_AUTHOR =                    'author'
    KEY_DATE =                      'date'
    KEY_PROJECT =                   'project'
    
    


    
    

    def __init__(self, sourceFile):
        ''' default constructor '''
        self.sourceFileName = sourceFile
        self.srcFile = open(self.sourceFileName)
        self.srcFileContents = self.srcFile.read()
        self.srcFile.close()
        self.quoteType = "\'"
                


    ################################################################
    ##    declaration of class-related tag manipulation methods   ##
    ################################################################


    def getAllClassTagData(self):
        ''' returns a list of all class data dictionary in given source file '''
        classTagDataList = []
        index = 0
        quoteType = self.quoteType
        classTag = self.TAG_CLASS
        while(True):
            try:
                ''' find next class tag '''
                index = self.srcFileContents.index(
                 classTag, index+1)
                classTagDataDict = self.getTagData(index)
                classTagDataList.append(classTagDataDict)
            except:
                break
        return classTagDataList

        
        


    def getClassMethodsTagData(self, className):
        ''' returns an array of all methods in given source file & class
            implement in sub-class
        '''
        quoteType = self.quoteType
        classMethodTag = self.TAG_CLASS_METHOD
        sourceData = self.srcFileContents
        methodTagDataList = []
        classStartIndex = self.getClassBlockIndexRange(className)[0]
        classEndIndex = self.getClassBlockIndexRange(className)[1]
        classMethodTagIndex = classStartIndex
        while(True):
            try:
                classMethodTagIndex = sourceData.index(
                    classMethodTag, classMethodTagIndex+1,
                    classEndIndex)
                methodTagDat = self.getTagData(classMethodTagIndex)
                methodTagDataList.append(methodTagDat)
            except:
                break
        return methodTagDataList


    

    def getClassMethodParametersTagData(self, className, methodName):
        ''' returns an array of all parameters dictionary of the given method '''
        quoteType = self.quoteType
        sourceData = self.srcFileContents
        methodStartIndex = self.getClassMethodBlockIndexRange(className, methodName)[0]
        methodEndIndex = self.getClassMethodBlockIndexRange(className, methodName)[1]
        paramTag = self.TAG_CLASS_METHOD_PARAM
        classMethodParamData = list()

        ''' now look for all attribute tags and respective tag data '''
        paramTagIndex = methodStartIndex
        while(True):
            try:
                paramTagIndex = sourceData.index(paramTag,
                    paramTagIndex+1, methodEndIndex)
                tagData = self.getTagData(paramTagIndex)
                classMethodParamData.append(tagData)
            except:
                break
        return classMethodParamData






    def getClassMethodReturnsTagData(self, className, methodName):
        ''' returns an array of all possible values & types returned by method
            implement in sub-class
        '''
        quoteType = self.quoteType
        sourceData = self.srcFileContents
        methodStartIndex = self.getClassMethodBlockIndexRange(className, methodName)[0]
        methodEndIndex = self.getClassMethodBlockIndexRange(className, methodName)[1]
        returnTag = self.TAG_CLASS_METHOD_RETURN
        classMethodReturnData = list()

        ''' now look for all attribute tags and respective tag data '''
        returnTagIndex = methodStartIndex
        while(True):
            try:
                returnTagIndex = sourceData.index(returnTag,
                    returnTagIndex+1, methodEndIndex)
                tagData = self.getTagData(returnTagIndex)
                classMethodReturnData.append(tagData)
            except:
                break
        return classMethodReturnData






    def getClassAttributesTagData(self, className):
        ''' returns an array of all attrib dictionaries
            in given source file & class
        '''
        quoteType = self.quoteType
        sourceData = self.srcFileContents
        classStartIndex = self.getClassBlockIndexRange(className)[0]
        classEndIndex = self.getClassBlockIndexRange(className)[1]
        attrTag = self.TAG_CLASS_ATTRIBUTE
        classAttrData = list()

        ''' now look for all attribute tags and respective tag data '''
        attrTagIndex = classStartIndex
        while(True):
            try:
                attrTagIndex = sourceData.index(attrTag,
                    attrTagIndex+1, classEndIndex)
                tagData = self.getTagData(attrTagIndex)
                classAttrData.append(tagData)
            except:
                break
        return classAttrData
        








    ####################################################################
    ##    declaration of non-class related tag manipulation methods   ##
    ####################################################################


    def getMethodsTagData(self):
        ''' returns an array of all non-class methods dictionary in given source file
        '''
        quoteType = self.quoteType
        MethodTag = self.TAG_METHOD
        sourceData = self.srcFileContents
        methodTagDataList = []
        startIndex = 0
        endIndex = len(sourceData)
        while(True):
            try:
                startIndex = sourceData.index(
                    MethodTag, startIndex+1,endIndex)
                methodTagDat = self.getTagData(startIndex)
                methodTagDataList.append(methodTagDat)
            except:
                break
        return methodTagDataList


    

    def getMethodParametersTagData(self, methodName):
        ''' returns an array of all parameters dictionary of the given method '''
        quoteType = self.quoteType
        sourceData = self.srcFileContents
        methodStartIndex = self.getMethodBlockIndexRange(methodName)[0]
        methodEndIndex = self.getMethodBlockIndexRange(methodName)[1]
        paramTag = self.TAG_METHOD_PARAM
        methodParamData = list()

        ''' now look for all attribute tags and respective tag data '''
        paramTagIndex = methodStartIndex
        while(True):
            try:
                paramTagIndex = sourceData.index(paramTag,
                    paramTagIndex+1, methodEndIndex)
                tagData = self.getTagData(paramTagIndex)
                methodParamData.append(tagData)
            except:
                break
        return methodParamData






    def getMethodReturnsTagData(self, methodName):
        ''' returns an array of all returns dictionary of the given method '''
        quoteType = self.quoteType
        sourceData = self.srcFileContents
        methodStartIndex = self.getMethodBlockIndexRange(methodName)[0]
        methodEndIndex = self.getMethodBlockIndexRange(methodName)[1]
        returnTag = self.TAG_METHOD_RETURN
        methodReturnData = list()

        ''' now look for all attribute tags and respective tag data '''
        returnTagIndex = methodStartIndex
        while(True):
            try:
                returnTagIndex = sourceData.index(returnTag,
                    returnTagIndex+1, methodEndIndex)
                tagData = self.getTagData(returnTagIndex)
                methodReturnData.append(tagData)
            except:
                break
        return methodReturnData




    def getAttributesTagData(self):
        ''' returns an array of all non-class attribs dictionaries
            in given source file
        '''
        quoteType = self.quoteType
        sourceData = self.srcFileContents
        startIndex = 0
        endIndex = len(sourceData)
        attrTag = self.TAG_ATTRIBUTE
        attrData = list()

        ''' now look for all attribute tags and respective tag data '''
        attrTagIndex = startIndex
        while(True):
            try:
                attrTagIndex = sourceData.index(attrTag,
                    attrTagIndex+1, endIndex)
                tagData = self.getTagData(attrTagIndex)
                attrData.append(tagData)
            except:
                break
        return attrData




    ####################################################################
    ##    declaration of methods for handling general file tags       ##
    ####################################################################


    def getSourceFileTagData(self):
        quoteType = self.quoteType
        sourceData = self.srcFileContents
        startIndex = 0
        endIndex = len(sourceData)
        fileTag = self.TAG_FILE
        fileData = list()

        '''now look for all attribute tags and respective tag data'''
        fileTagIndex = startIndex
        try:
            fileTagIndex = sourceData.index(fileTag,
                fileTagIndex+1, endIndex)
            tagData = self.getTagData(fileTagIndex)
            fileData.append(tagData)
            return fileData
        except:
            return ""


    
        

    def getSourceFileContributorTagData(self):
        quoteType = self.quoteType
        sourceData = self.srcFileContents
        startIndex = 0
        endIndex = len(sourceData)
        contributorTag = self.TAG_CONTRIBUTOR
        contributorData = list()

        '''now look for all attribute tags and respective tag data'''
        contributorTagIndex = startIndex
        while(True):
            try:
                contributorTagIndex = sourceData.index(contributorTag,
                    contributorTagIndex+1, endIndex)
                tagData = self.getTagData(contributorTagIndex)
                contributorData.append(tagData)
            except:
                break
        return contributorData
















    ####################################################################
    ##                declaration of helper methods                   ##
    ####################################################################


    # the following methods are helper methods.
    def getTagData(self, tagIndex):
        quoteType = self.quoteType
        try:
            leftQuoteIndex = self.srcFileContents.index(
                quoteType,tagIndex)
            
            rightQuoteIndex = self.srcFileContents.index(
                quoteType, leftQuoteIndex+1)
            
            tagDataStr = self.srcFileContents[leftQuoteIndex:
                rightQuoteIndex+1]
            
            tagDataStr = tagDataStr.replace(quoteType,"")
            tagDataStr = tagDataStr.replace("\n","")
            tagDataFormattedStr = str()
            tagDataDictionary = dict()
            
            ''' format class tag data into list '''
            for data in tagDataStr.split(","):
                data = data.replace("\n","")
                data = data.strip()
                key,val = data.split('=')
                tagDataDictionary[key]=val
            return tagDataDictionary
        
        except:
            return dict()
        






    

    def getClassBlockIndexRange(self,className):
        classStartIndex = int()
        classEndIndex = int()
        sourceData = self.srcFileContents
        quoteType = self.quoteType
        classTag = self.TAG_CLASS
        classTagNameKey = self.KEY_NAME

        ''' get class start index '''
        while(True):
            try:
                classStartIndex = sourceData.index(classTag,
                    classStartIndex+1)
                tagData = self.getTagData(classStartIndex)
                kValue = tagData[classTagNameKey]
                if(kValue == className):
                    try:
                        classEndIndex = sourceData.index(classTag,
                            classStartIndex+1)
                    except:
                        classEndIndex = len(sourceData)-1
                    
                    return [classStartIndex, classEndIndex]
            except:
                ''' no more class tags and '''
                return []
        
            


    def getClassMethodBlockIndexRange(self, className, methodName):
        quoteType = self.quoteType
        classStartIndex = self.getClassBlockIndexRange(className)[0]
        classEndIndex = self.getClassBlockIndexRange(className)[1]
        methodStartIndex = int()
        methodEndIndex = int()
        sourceData = self.srcFileContents
        classMethodTag = self.TAG_CLASS_METHOD
        classMethodTagNameKey = self.KEY_NAME

        ''' get class method start index '''
        classMethodStartIndex = classStartIndex
        while(True):
            try:
                classMethodStartIndex = sourceData.index(classMethodTag,
                    classMethodStartIndex+1)
                tagData = self.getTagData(classMethodStartIndex)
                kValue = tagData[classMethodTagNameKey]
                if(kValue == methodName):
                    ''' now look for end index of method '''
                    try:
                        classMethodEndIndex = sourceData.index(classMethodTag,
                            classMethodStartIndex+1)
                    except:
                        classMethodEndIndex = len(sourceData)-1
                    
                    return [classMethodStartIndex, classMethodEndIndex]
            except:
                ''' no more class tags and '''
                return []

    def getMethodBlockIndexRange(self, methodName):
        ''' returns a list with start-end indexes of a method tag based on name key '''
        quoteType = self.quoteType
        sourceData = self.srcFileContents
        startIndex = 0
        endIndex = len(sourceData)
        methodTag = self.TAG_METHOD
        methodNameKey = self.KEY_NAME
        methodStartIndex = int()
        methodEndIndex = int()

        ''' get method start index '''
        methodStartIndex = startIndex
        while(True):
            try:
                methodStartIndex = sourceData.index(methodTag,
                    methodStartIndex+1, endIndex)
                tagData = self.getTagData(methodStartIndex)
                methodNameValue = tagData[methodNameKey]
                if(methodNameValue == methodName):
                    ''' now look for method end index '''
                    try:
                        methodEndIndex = sourceData.index(methodTag,
                            methodStartIndex+1)
                    except:
                        methodEndIndex = endIndex
                    return [methodStartIndex, methodEndIndex]
            except:
                ''' no more method tags '''
                return []
