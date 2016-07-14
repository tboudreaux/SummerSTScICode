from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[241.121292,10.000583],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_160429.11+100002.1/sdB_sdssj9-10_160429.11+100002.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_160429.11+100002.1/sdB_sdssj9-10_160429.11+100002.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
