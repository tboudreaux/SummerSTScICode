from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[221.907292,2.161833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_144737.75+020942.6/sdB_sdssj_144737.75+020942.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_144737.75+020942.6/sdB_sdssj_144737.75+020942.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
