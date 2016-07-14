from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[166.465375,36.342294],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_cbs_135/sdB_cbs_135_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_cbs_135/sdB_cbs_135_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()