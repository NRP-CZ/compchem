import { isObjectArrayWithNesting } from '@jsonforms/core';

const MatrixTester = (uischema, schema, context) => {
        if (isObjectArrayWithNesting(uischema, schema, context)) {
            return 69;
        }
        return -1;
    };
  
export default MatrixTester;
