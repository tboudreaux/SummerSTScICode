from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[217.588667,48.86075],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_cbs_272/sdB_cbs_272_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_cbs_272/sdB_cbs_272_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
