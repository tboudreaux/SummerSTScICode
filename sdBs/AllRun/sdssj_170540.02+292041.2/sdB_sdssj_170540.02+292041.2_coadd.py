from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[256.41675,29.344778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_170540.02+292041.2/sdB_sdssj_170540.02+292041.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_170540.02+292041.2/sdB_sdssj_170540.02+292041.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
