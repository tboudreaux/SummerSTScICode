from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[310.9965,-10.795192],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_[l92b]_marka/sdB_[l92b]_marka_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_[l92b]_marka/sdB_[l92b]_marka_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
