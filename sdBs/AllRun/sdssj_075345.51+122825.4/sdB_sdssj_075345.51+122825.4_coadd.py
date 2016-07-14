from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[118.439625,12.473722],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_075345.51+122825.4/sdB_sdssj_075345.51+122825.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_075345.51+122825.4/sdB_sdssj_075345.51+122825.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
