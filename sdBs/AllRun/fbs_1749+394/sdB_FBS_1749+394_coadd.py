from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[267.866542,39.387056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_1749+394/sdB_FBS_1749+394_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_1749+394/sdB_FBS_1749+394_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
