from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[353.922792,0.038722],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_233541.47+000219.4/sdB_sdssj_233541.47+000219.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_233541.47+000219.4/sdB_sdssj_233541.47+000219.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
