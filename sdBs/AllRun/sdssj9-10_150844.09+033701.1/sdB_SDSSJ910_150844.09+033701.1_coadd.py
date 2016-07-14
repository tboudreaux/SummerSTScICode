from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[227.183708,3.616972],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_150844.09+033701.1/sdB_SDSSJ910_150844.09+033701.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_150844.09+033701.1/sdB_SDSSJ910_150844.09+033701.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
