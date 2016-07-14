from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[239.768458,18.759556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_155904.43+184534.4/sdB_sdssj9-10_155904.43+184534.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_155904.43+184534.4/sdB_sdssj9-10_155904.43+184534.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
