from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[244.520542,20.684472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_161804.93+204104.1/sdB_sdssj9-10_161804.93+204104.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_161804.93+204104.1/sdB_sdssj9-10_161804.93+204104.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
