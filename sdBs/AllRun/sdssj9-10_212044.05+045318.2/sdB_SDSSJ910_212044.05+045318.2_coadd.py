from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[320.183542,4.888389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_212044.05+045318.2/sdB_SDSSJ910_212044.05+045318.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_212044.05+045318.2/sdB_SDSSJ910_212044.05+045318.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
