from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[136.783417,-3.104417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_uvo_0904-02/sdB_uvo_0904-02_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_uvo_0904-02/sdB_uvo_0904-02_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
