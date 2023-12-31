import PropTypes from 'prop-types';
import "../style/card.css"
import "../style/cardreceta.css"

const Cardreceta = ({ foto, titulo, paso1, recetaRef}) => {
  return (
    <>
      <div ref={recetaRef} className="receta container card mb-3" >
        <div className="row g-0">
          <div className="col-md-3 d-flex align-items-center justify-content-center">
            <img src={foto} className="shrink img-fluid rounded-start m-3" alt="..." />
          </div>
          <div className="col-md-8"> 
            <div className="card-body ">
              <h2 className="card-title">{titulo}</h2>
              <p className="pasos card-text">
                <pre className='pasos col-12'>{paso1}</pre>
              </p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

Cardreceta.propTypes = {
  foto: PropTypes.any,
  titulo: PropTypes.any,
  paso1: PropTypes.any,
  recetaRef:PropTypes.any,
};

export default Cardreceta;
