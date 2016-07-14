from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[117.722,14.804167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_075053.28+144815.0/sdB_SDSSJ_075053.28+144815.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_075053.28+144815.0/sdB_SDSSJ_075053.28+144815.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
