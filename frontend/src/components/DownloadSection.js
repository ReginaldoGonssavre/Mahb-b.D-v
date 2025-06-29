import React from 'react';
import { useTranslation } from 'react-i18next';

const DownloadSection = ({ t }) => (
  <section className="download-section">
    <h2>{t('download_software_title')}</h2>
    <div className="download-buttons">
      <a href="/aigro-quantum-saas-free.zip" download>
        <button>{t('download_free_button')}</button>
      </a>
      <a href="/aigro-quantum-saas-paid.zip" download>
        <button>{t('download_paid_button')}</button>
      </a>
    </div>
  </section>
);

export default DownloadSection;